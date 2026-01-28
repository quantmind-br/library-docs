---
title: mitmproxy.addonmanager
url: https://docs.mitmproxy.org/stable/api/mitmproxy/addonmanager.html
source: crawler
fetched_at: 2026-01-28T15:59:15.866616824-03:00
rendered_js: false
word_count: 1665
summary: This document defines the addon management system for mitmproxy, including classes and functions for loading, registering, and managing addons within the proxy framework.
tags:
    - addon-manager
    - plugin-system
    - lifecycle-events
    - configuration
category: reference
---

[Edit on GitHub](https://github.com/mitmproxy/mitmproxy/blob/main/mitmproxy/addonmanager.py) View Source

```
  1importcontextlib
  2importinspect
  3importlogging
  4importpprint
  5importsys
  6importtraceback
  7importtypes
  8fromcollections.abcimport Callable
  9fromcollections.abcimport Sequence
 10fromdataclassesimport dataclass
 11fromtypingimport Any
 12
 13frommitmproxyimport exceptions
 14frommitmproxyimport flow
 15frommitmproxyimport hooks
 16
 17logger = logging.getLogger(__name__)
 18
 19
 20def_get_name(itm):
 21    return getattr(itm, "name", itm.__class__.__name__.lower())
 22
 23
 24defcut_traceback(tb, func_name):
 25"""
 26    Cut off a traceback at the function with the given name.
 27    The func_name's frame is excluded.
 28
 29    Args:
 30        tb: traceback object, as returned by sys.exc_info()[2]
 31        func_name: function name
 32
 33    Returns:
 34        Reduced traceback.
 35    """
 36    tb_orig = tb
 37    for _, _, fname, _ in traceback.extract_tb(tb):
 38        tb = tb.tb_next
 39        if fname == func_name:
 40            break
 41    return tb or tb_orig
 42
 43
 44@contextlib.contextmanager
 45defsafecall():
 46    try:
 47        yield
 48    except (exceptions.AddonHalt, exceptions.OptionsError):
 49        raise
 50    except Exception:
 51        etype, value, tb = sys.exc_info()
 52        tb = cut_traceback(tb, "invoke_addon_sync")
 53        tb = cut_traceback(tb, "invoke_addon")
 54        assert etype
 55        assert value
 56        logger.error(
 57            f"Addon error: {value}",
 58            exc_info=(etype, value, tb),
 59        )
 60
 61
 62classLoader:
 63"""
 64    A loader object is passed to the load() event when addons start up.
 65    """
 66
 67    def__init__(self, master):
 68        self.master = master
 69
 70    defadd_option(
 71        self,
 72        name: str,
 73        typespec: type,
 74        default: Any,
 75        help: str,
 76        choices: Sequence[str] | None = None,
 77    ) -> None:
 78"""
 79        Add an option to mitmproxy.
 80
 81        Help should be a single paragraph with no linebreaks - it will be
 82        reflowed by tools. Information on the data type should be omitted -
 83        it will be generated and added by tools as needed.
 84        """
 85        assert not isinstance(choices, str)
 86        if name in self.master.options:
 87            existing = self.master.options._options[name]
 88            same_signature = (
 89                existing.name == name
 90                and existing.typespec == typespec
 91                and existing.default == default
 92                and existing.help == help
 93                and existing.choices == choices
 94            )
 95            if same_signature:
 96                return
 97            else:
 98                logger.warning("Over-riding existing option %s" % name)
 99        self.master.options.add_option(name, typespec, default, help, choices)
100
101    defadd_command(self, path: str, func: Callable) -> None:
102"""Add a command to mitmproxy.
103
104        Unless you are generating commands programatically,
105        this API should be avoided. Decorate your function with `@mitmproxy.command.command` instead.
106        """
107        self.master.commands.add(path, func)
108
109
110deftraverse(chain):
111"""
112    Recursively traverse an addon chain.
113    """
114    for a in chain:
115        yield a
116        if hasattr(a, "addons"):
117            yield from traverse(a.addons)
118
119
120@dataclass
121classLoadHook(hooks.Hook):
122"""
123    Called when an addon is first loaded. This event receives a Loader
124    object, which contains methods for adding options and commands. This
125    method is where the addon configures itself.
126    """
127
128    loader: Loader
129
130
131classAddonManager:
132    def__init__(self, master):
133        self.lookup = {}
134        self.chain = []
135        self.master = master
136        master.options.changed.connect(self._configure_all)
137
138    def_configure_all(self, updated):
139        self.trigger(hooks.ConfigureHook(updated))
140
141    defclear(self):
142"""
143        Remove all addons.
144        """
145        for a in self.chain:
146            self.invoke_addon_sync(a, hooks.DoneHook())
147        self.lookup = {}
148        self.chain = []
149
150    defget(self, name):
151"""
152        Retrieve an addon by name. Addon names are equal to the .name
153        attribute on the instance, or the lower case class name if that
154        does not exist.
155        """
156        return self.lookup.get(name, None)
157
158    defregister(self, addon):
159"""
160        Register an addon, call its load event, and then register all its
161        sub-addons. This should be used by addons that dynamically manage
162        addons.
163
164        If the calling addon is already running, it should follow with
165        running and configure events. Must be called within a current
166        context.
167        """
168        api_changes = {
169            # mitmproxy 6 -> mitmproxy 7
170            "clientconnect": f"The clientconnect event has been removed, use client_connected instead",
171            "clientdisconnect": f"The clientdisconnect event has been removed, use client_disconnected instead",
172            "serverconnect": "The serverconnect event has been removed, use server_connect and server_connected instead",
173            "serverdisconnect": f"The serverdisconnect event has been removed, use server_disconnected instead",
174            # mitmproxy 8 -> mitmproxy 9
175            "add_log": "The add_log event has been deprecated, use Python's builtin logging module instead",
176        }
177        for a in traverse([addon]):
178            for old, msg in api_changes.items():
179                if hasattr(a, old):
180                    logger.warning(
181                        f"{msg}. For more details, see https://docs.mitmproxy.org/dev/addons-api-changelog/."
182                    )
183            name = _get_name(a)
184            if name in self.lookup:
185                raise exceptions.AddonManagerError(
186                    "An addon called '%s' already exists." % name
187                )
188        loader = Loader(self.master)
189        self.invoke_addon_sync(addon, LoadHook(loader))
190        for a in traverse([addon]):
191            name = _get_name(a)
192            self.lookup[name] = a
193        for a in traverse([addon]):
194            self.master.commands.collect_commands(a)
195        self.master.options.process_deferred()
196        return addon
197
198    defadd(self, *addons):
199"""
200        Add addons to the end of the chain, and run their load event.
201        If any addon has sub-addons, they are registered.
202        """
203        for i in addons:
204            self.chain.append(self.register(i))
205
206    defremove(self, addon):
207"""
208        Remove an addon and all its sub-addons.
209
210        If the addon is not in the chain - that is, if it's managed by a
211        parent addon - it's the parent's responsibility to remove it from
212        its own addons attribute.
213        """
214        for a in traverse([addon]):
215            n = _get_name(a)
216            if n not in self.lookup:
217                raise exceptions.AddonManagerError("No such addon: %s" % n)
218            self.chain = [i for i in self.chain if i is not a]
219            del self.lookup[_get_name(a)]
220        self.invoke_addon_sync(addon, hooks.DoneHook())
221
222    def__len__(self):
223        return len(self.chain)
224
225    def__str__(self):
226        return pprint.pformat([str(i) for i in self.chain])
227
228    def__contains__(self, item):
229        name = _get_name(item)
230        return name in self.lookup
231
232    async defhandle_lifecycle(self, event: hooks.Hook):
233"""
234        Handle a lifecycle event.
235        """
236        message = event.args()[0]
237
238        await self.trigger_event(event)
239
240        if isinstance(message, flow.Flow):
241            await self.trigger_event(hooks.UpdateHook([message]))
242
243    def_iter_hooks(self, addon, event: hooks.Hook):
244"""
245        Enumerate all hook callables belonging to the given addon
246        """
247        assert isinstance(event, hooks.Hook)
248        for a in traverse([addon]):
249            func = getattr(a, event.name, None)
250            if func:
251                if callable(func):
252                    yield a, func
253                elif isinstance(func, types.ModuleType):
254                    # we gracefully exclude module imports with the same name as hooks.
255                    # For example, a user may have "from mitmproxy import log" in an addon,
256                    # which has the same name as the "log" hook. In this particular case,
257                    # we end up in an error loop because we "log" this error.
258                    pass
259                else:
260                    raise exceptions.AddonManagerError(
261                        f"Addon handler {event.name} ({a}) not callable"
262                    )
263
264    async definvoke_addon(self, addon, event: hooks.Hook):
265"""
266        Asynchronously invoke an event on an addon and all its children.
267        """
268        for addon, func in self._iter_hooks(addon, event):
269            res = func(*event.args())
270            # Support both async and sync hook functions
271            if res is not None and inspect.isawaitable(res):
272                await res
273
274    definvoke_addon_sync(self, addon, event: hooks.Hook):
275"""
276        Invoke an event on an addon and all its children.
277        """
278        for addon, func in self._iter_hooks(addon, event):
279            if inspect.iscoroutinefunction(func):
280                raise exceptions.AddonManagerError(
281                    f"Async handler {event.name} ({addon}) cannot be called from sync context"
282                )
283            func(*event.args())
284
285    async deftrigger_event(self, event: hooks.Hook):
286"""
287        Asynchronously trigger an event across all addons.
288        """
289        for i in self.chain:
290            try:
291                with safecall():
292                    await self.invoke_addon(i, event)
293            except exceptions.AddonHalt:
294                return
295
296    deftrigger(self, event: hooks.Hook):
297"""
298        Trigger an event across all addons.
299
300        This API is discouraged and may be deprecated in the future.
301        Use `trigger_event()` instead, which provides the same functionality but supports async hooks.
302        """
303        for i in self.chain:
304            try:
305                with safecall():
306                    self.invoke_addon_sync(i, event)
307            except exceptions.AddonHalt:
308                return
```

class Loader: View Source

[](#Loader)

```
 63classLoader:
 64"""
 65    A loader object is passed to the load() event when addons start up.
 66    """
 67
 68    def__init__(self, master):
 69        self.master = master
 70
 71    defadd_option(
 72        self,
 73        name: str,
 74        typespec: type,
 75        default: Any,
 76        help: str,
 77        choices: Sequence[str] | None = None,
 78    ) -> None:
 79"""
 80        Add an option to mitmproxy.
 81
 82        Help should be a single paragraph with no linebreaks - it will be
 83        reflowed by tools. Information on the data type should be omitted -
 84        it will be generated and added by tools as needed.
 85        """
 86        assert not isinstance(choices, str)
 87        if name in self.master.options:
 88            existing = self.master.options._options[name]
 89            same_signature = (
 90                existing.name == name
 91                and existing.typespec == typespec
 92                and existing.default == default
 93                and existing.help == help
 94                and existing.choices == choices
 95            )
 96            if same_signature:
 97                return
 98            else:
 99                logger.warning("Over-riding existing option %s" % name)
100        self.master.options.add_option(name, typespec, default, help, choices)
101
102    defadd_command(self, path: str, func: Callable) -> None:
103"""Add a command to mitmproxy.
104
105        Unless you are generating commands programatically,
106        this API should be avoided. Decorate your function with `@mitmproxy.command.command` instead.
107        """
108        self.master.commands.add(path, func)
```

A loader object is passed to the load() event when addons start up.

def add\_option( self, name: str, typespec: type, default: Any, help: str, choices: Sequence\[str] | None = None) -&gt; None: View Source

```
 71    defadd_option(
 72        self,
 73        name: str,
 74        typespec: type,
 75        default: Any,
 76        help: str,
 77        choices: Sequence[str] | None = None,
 78    ) -> None:
 79"""
 80        Add an option to mitmproxy.
 81
 82        Help should be a single paragraph with no linebreaks - it will be
 83        reflowed by tools. Information on the data type should be omitted -
 84        it will be generated and added by tools as needed.
 85        """
 86        assert not isinstance(choices, str)
 87        if name in self.master.options:
 88            existing = self.master.options._options[name]
 89            same_signature = (
 90                existing.name == name
 91                and existing.typespec == typespec
 92                and existing.default == default
 93                and existing.help == help
 94                and existing.choices == choices
 95            )
 96            if same_signature:
 97                return
 98            else:
 99                logger.warning("Over-riding existing option %s" % name)
100        self.master.options.add_option(name, typespec, default, help, choices)
```

Add an option to mitmproxy.

Help should be a single paragraph with no linebreaks - it will be reflowed by tools. Information on the data type should be omitted - it will be generated and added by tools as needed.

def add\_command(self, path: str, func: Callable) -&gt; None: View Source

```
102    defadd_command(self, path: str, func: Callable) -> None:
103"""Add a command to mitmproxy.
104
105        Unless you are generating commands programatically,
106        this API should be avoided. Decorate your function with `@mitmproxy.command.command` instead.
107        """
108        self.master.commands.add(path, func)
```

Add a command to mitmproxy.

Unless you are generating commands programatically, this API should be avoided. Decorate your function with `@mitmproxy.command.command` instead.