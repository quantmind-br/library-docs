---
title: Comprehensive keyboard handling in terminals
title: Keyboard protocol
word_count: 4182
summary: This document introduces the kitty keyboard protocol, a comprehensive and backward-compatible specification designed to resolve ambiguity and limitations in traditional terminal keyboard event handling.
category: concept
optimized: true
optimized_at: 2026-05-04T20:46:25Z
---
optimized: true
optimized_at: 2026-05-04T18:00:00Z
# Comprehensive keyboard handling in terminals

There are various problems with the current state of keyboard handling in
terminals. They include:

- No way to use modifiers other than `ctrl` and `alt`

- No way to reliably use multiple modifier keys, other than, `shift+alt` and
  `ctrl+alt`.

- Many of the existing escape codes used to encode these events are ambiguous
  with different key presses mapping to the same escape code.

- No way to handle different types of keyboard events, such as press, release or repeat

- No reliable way to distinguish single `Esc` key presses from the start of a
  escape sequence. Currently, client programs use fragile timing related hacks
  for this, leading to bugs, for example:
  [neovim #2035](https://github.com/neovim/neovim/issues/2035).

To solve these issues and others, kitty has created a new keyboard protocol,
that is backward compatible but allows applications to opt-in to support more
advanced usages. The protocol is based on initial work in `fixterms
<http://www.leonerd.org.uk/hacks/fixterms/>`_, however, it corrects various
issues in that proposal, listed at the :ref:`bottom of this document
<fixterms_bugs>`. For public discussion of this spec, see 3248.

You can see this protocol with all enhancements in action by running:

```
kitten show-key -m kitty
```

inside the kitty terminal to report key events.

In addition to kitty, this protocol is also implemented in:

- The [alacritty terminal](https://github.com/alacritty/alacritty/pull/7125)
- The [foot terminal](https://codeberg.org/dnkl/foot/issues/319)
- The [ghostty terminal](https://ghostty.org)
- The [iTerm2 terminal](https://gitlab.com/gnachman/iterm2/-/issues/10017)
- The [Microsoft terminal](https://github.com/microsoft/terminal/pull/19817)
- The [rio terminal](https://github.com/raphamorim/rio/commit/cd463ca37677a0fc48daa8795ea46dadc92b1e95)
- The [TuiOS terminal (multiplexer)](https://github.com/Gaurav-Gosain/tuios/issues/26)
- The [Warp terminal](https://github.com/warpdotdev/Warp/issues/8462#issuecomment-3857779488)
- The [WezTerm terminal](https://wezfurlong.org/wezterm/config/lua/config/enable_kitty_keyboard.html)
- The [xterm.js terminal](https://github.com/xtermjs/xterm.js/pull/5600)

Libraries implementing this protocol:

- The [notcurses library](https://github.com/dankamongmen/notcurses/issues/2131)
- The [crossterm library](https://github.com/crossterm-rs/crossterm/pull/688)
- The [textual library](https://github.com/Textualize/textual/pull/4631)
- The vaxis library [go](https://sr.ht/~rockorager/vaxis/) and [zig](https://github.com/rockorager/libvaxis/)
- The [bubbletea library](https://github.com/charmbracelet/bubbletea/issues/869)
- The [vtinput](https://unxed.github.com/vtinput) and [vtui](https://github.com/unxed/vtui) libraries
- The [tcell library](https://github.com/gdamore/tcell/commit/c10909b991eb87c009554fe9b2dfa7276e2649c1)

Programs implementing this protocol:

- The [Vim text editor](https://github.com/vim/vim/commit/63a2e360cca2c70ab0a85d14771d3259d4b3aafa)
- The [Emacs text editor via the kkp package](https://github.com/benjaminor/kkp)
- The [Neovim text editor](https://github.com/neovim/neovim/pull/18181)
- The [kakoune text editor](https://github.com/mawww/kakoune/issues/4103)
- The [dte text editor](https://gitlab.com/craigbarnes/dte/-/issues/138)
- The [Helix text editor](https://github.com/helix-editor/helix/pull/4939)
- The [Flow control editor](https://github.com/neurocyte/flow?tab=readme-ov-file#requirements)
- The [far2l](https://github.com/elfmz/far2l/commit/e1f2ee0ef2b8332e5fa3ad7f2e4afefe7c96fc3b) and [f4](https://github.com/unxed/f4) file managers
- The [Yazi file manager](https://github.com/sxyazi/yazi)
- The [awrit web browser](https://github.com/chase/awrit)
- The [Turbo Vision](https://github.com/magiblot/tvision/commit/6e5a7b46c6634079feb2ac98f0b890bbed59f1ba)/[Free Vision](https://gitlab.com/freepascal.org/fpc/source/-/issues/40673#note_2061428120) IDEs
- The [aerc email client](https://git.sr.ht/~rjarry/aerc/commit/d73cf33c2c6c3e564ce8aff04acc329a06eafc54)

Shells implementing this protocol:

- The [nushell shell](https://github.com/nushell/nushell/pull/10540)
- The [fish shell](https://github.com/fish-shell/fish-shell/commit/8bf8b10f685d964101f491b9cc3da04117a308b4)

## Quickstart

If you are an application or library developer just interested in using this
protocol to make keyboard handling simpler and more robust in your application,
without too many changes, do the following:

1. Emit the escape code `CSI > 1 u` at application startup if using the main
   screen or when entering alternate screen mode, if using the alternate
   screen.
1. All key events will now be sent in only a few forms to your application,
   that are easy to parse unambiguously.
1. Emit the escape sequence `CSI < u` at application exit if using the main
   screen or just before leaving alternate screen mode if using the alternate screen,
   to restore whatever the keyboard mode was before step 1.

Key events will all be delivered to your application either as plain UTF-8
text, or using the following escape codes, for those keys that do not produce
text (`CSI` is the bytes `0x1b 0x5b`):

```
CSI number ; modifiers [u~]
CSI 1; modifiers [ABCDEFHPQS]
0x0d - for the Enter key
0x7f or 0x08 - for Backspace
0x09 - for Tab
```

The `number` in the first form above will be either the Unicode codepoint for a
key, such as `97` for the a key, or one of the numbers from the
functional table below. The `modifiers` optional parameter encodes any
modifiers active for the key event. The encoding is described in the
modifiers section.

The second form is used for a few functional keys, such as the Home,
End, Arrow keys and F1 ... F4, they are enumerated in
the functional table below.  Note that if no modifiers are present the
parameters are omitted entirely giving an escape code of the form ``CSI
[ABCDEFHPQS]``.

If you want support for more advanced features such as repeat and release
events, alternate keys for shortcut matching et cetera, these can be turned on
using progressive_enhancement as documented in the rest of this
specification.

## An overview

Key events are divided into two types, those that produce text and those that
do not. When a key event produces text, the text is sent directly as UTF-8
encoded bytes. This is safe as UTF-8 contains no C0 control codes.
When the key event does not have text, the key event is encoded as an escape code. In
legacy compatibility mode (the default) this uses legacy escape codes, so old terminal
applications continue to work. For more advanced features, such as release/repeat
reporting etc., applications can tell the terminal they want this information by
sending an escape code to progressively enhance <progressive_enhancement> the data reported for
key events.

The central escape code used to encode key events is:

```
CSI unicode-key-code:alternate-key-codes ; modifiers:event-type ; text-as-codepoints u
```

Spaces in the above definition are present for clarity and should be ignored.
`CSI` is the bytes `0x1b 0x5b`. All parameters are decimal numbers. Fields
are separated by the semi-colon and sub-fields by the colon. Only the
`unicode-key-code` field is mandatory, everything else is optional. The
escape code is terminated by the `u` character (the byte `0x75`).

### Key codes

The `unicode-key-code` above is the Unicode codepoint representing the key, as a
decimal number. For example, the A key is represented as `97` which is
the unicode code for lowercase `a`. Note that the codepoint used is *always*
the lower-case (or more technically, un-shifted) version of the key. If the
user presses, for example, ctrl+shift+a the escape code would be ``CSI
97;modifiers u`. It *must not* be `CSI 65; modifiers u``.

If *alternate key reporting* is requested by the program running in the
terminal, the terminal can send two additional Unicode codepoints, the *shifted
key* and *base layout key*, separated by colons. The shifted key is simply the
upper-case version of `unicode-codepoint`, or more technically, the shifted
version, in the currently active keyboard layout. So `a` becomes `A` and so on,
based on the current keyboard layout. This is needed to be able to match
against a shortcut such as ctrl+plus which depending on the type of
keyboard could be either ctrl+shift+equal or ctrl+plus. Note that
the shifted key must be present only if shift is also present in the modifiers.

The *base layout key* is the key corresponding to the physical key in the
standard PC-101 key layout. So for example, if the user is using a Cyrillic
keyboard with a Cyrillic keyboard layout pressing the ctrl+С key will
be ctrl+c in the standard layout. So the terminal should send the *base
layout key* as `99` corresponding to the `c` key.

If only one alternate key is present, it is the *shifted key*. If the terminal
wants to send only a base layout key but no shifted key, it must use an empty
sub-field for the shifted key, like this:

```
CSI unicode-key-code::base-layout-key
```

### Modifiers

This protocol supports six modifier keys, shift, alt,
ctrl, super, hyper, meta, num_lock and
caps_lock. Here super is either the *Windows/Linux* key or the
command key on mac keyboards. The alt key is the option
key on mac keyboards. hyper and meta are typically present only
on X11/Wayland based systems with special XKB rules. Modifiers are encoded as a
bit field with:

```
shift     0b1         (1)
alt       0b10        (2)
ctrl      0b100       (4)
super     0b1000      (8)
hyper     0b10000     (16)
meta      0b100000    (32)
caps_lock 0b1000000   (64)
num_lock  0b10000000  (128)
```

In the escape code, the modifier value is encoded as a decimal number which is
`1 + actual modifiers`. So to represent shift only, the value would be
`1 + 1 = 2`, to represent ctrl+shift the value would be ``1 + 0b101 =
6`` and so on. If the modifier field is not present in the escape code, its
default value is `1` which means no modifiers. If a modifier is *active* when
the key event occurs, i.e. if the key is pressed or the lock (for caps lock/num
lock) is enabled, the key event must have the bit for that modifier set.

When the key event is related to an actual modifier key, the corresponding
modifier's bit must be set to the modifier state including the effect for the
current event. For example, when pressing the LEFT_CONTROL key, the
`ctrl` bit must be set and when releasing it, it must be reset. When both
left and right control keys are pressed and one is released, the release event
must have the `ctrl` bit set. See 6913 for discussion of this design.

### Event types

There are three key event types: `press, repeat and release`. They are
reported (if requested `0b10`) as a sub-field of the modifiers field
(separated by a colon). If no modifiers are present, the modifiers field must
have the value `1` and the event type sub-field the type of event. The
`press` event type has value `1` and is the default if no event type sub
field is present. The `repeat` type is `2` and the `release` type is
`3`. So for example:

```
CSI key-code             # this is a press event
CSI key-code;modifier    # this is a press event
CSI key-code;modifier:1  # this is a press event
CSI key-code;modifier:2  # this is a repeat event
CSI key-code;modifier:3  # this is a release event
```

> [!NOTE]
> Key events that result in text are reported as plain UTF-8 text, so
>
> events are not supported for them, unless the application requests *key
> report mode*, see below.

### Text as code points

The terminal can optionally send the text associated with key events as a
sequence of Unicode code points. This behavior is opt-in by the :ref:`progressive
enhancement <progressive_enhancement>` mechanism described below. Some examples:

```
shift+a -> CSI 97 ; 2 ; 65 u   # The text 'A' is reported as 65
alt+a   -> CSI  0 ;   ; 229 u  # The text 'å' is reported as 229
```

If multiple code points are present, they must be separated by colons.  If no
known key is associated with the text the key number `0` must be used. The
associated text must not contain control codes (control codes are code points
below U+0020 and codepoints in the C0 and C1 blocks). In the above example, the
alt modifier is consumed by the OS itself to produce the text å and not
sent to the terminal emulator, which gets only a "text input" event and no
information about modifiers, thus the event gets encoded with no modifiers.
The exact behavior in these situations depends on the OS, keyboard layout, IME
system in use and so on. In general, if the terminal emulator receives no key
information, the key number 0 must be used to indicate a pure "text event".

### Non-Unicode keys

There are many keys that don't correspond to letters from human languages, and
thus aren't represented in Unicode. Think of functional keys, such as
Escape, Play, Pause, F1, Home, etc. These
are encoded using Unicode code points from the Private Use Area (``57344 -
63743``). The mapping of key names to code points for these keys is in the
Functional key definition table below <functional>.

## Progressive enhancement

While, in theory, every key event could be completely represented by this
protocol and all would be hunk-dory, in reality there is a vast universe of
existing terminal programs that expect legacy control codes for key events and
that are not likely to ever be updated. To support these, in default mode,
the terminal will emit legacy escape codes for compatibility. If a terminal
program wants more robust key handling, it can request it from the terminal,
via the mechanism described here. Each enhancement is described in detail
below. The escape code for requesting enhancements is:

```
CSI = flags ; mode u
```

Here `flags` is a decimal encoded integer to specify a set of bit-flags. The
meanings of the flags are given below. The second, `mode` parameter is
optional (defaulting to `1`) and specifies how the flags are applied.
The value `1` means all set bits are set and all unset bits are reset.
The value `2` means all set bits are set, unset bits are left unchanged.
The value `3` means all set bits are reset, unset bits are left unchanged.

The program running in the terminal can query the terminal for the
current values of the flags by sending:

```
CSI ? u
```

The terminal will reply with:

```
CSI ? flags u
```

The program can also push/pop the current flags onto a stack in the
terminal with:

```
CSI > flags u  # for push, if flags omitted default to zero
CSI < number u # to pop number entries, defaulting to 1 if unspecified
```

Terminals should limit the size of the stack as appropriate, to prevent
Denial-of-Service attacks. Terminals must maintain separate stacks for the main
and alternate screens. If a pop request is received that empties the stack,
all flags are reset. If a push request is received and the stack is full, the
oldest entry from the stack must be evicted.

> [!NOTE]
> The main and alternate screens in the terminal emulator must maintain
>
> their own, independent, keyboard mode stacks. This is so that a program that
> uses the alternate screen such as an editor, can change the keyboard mode
> in the alternate screen only, without affecting the mode in the main screen
> or even knowing what that mode is. Without this, and if no stack is
> implemented for keyboard modes (such as in some legacy terminal emulators)
> the editor would have to somehow know what the keyboard mode of the main
> screen is and restore to that mode on exit.

### Disambiguate escape codes

This type of progressive enhancement (`0b1`) fixes the problem of some legacy key press
encodings overlapping with other control codes. For instance, pressing the
Esc key generates the byte `0x1b` which also is used to indicate the
start of an escape code. Similarly pressing the key alt+[ will generate
the bytes used for CSI control codes.

Turning on this flag will cause the terminal to report the Esc, alt+key,
ctrl+key, ctrl+alt+key, shift+alt+key keys using `CSI u` sequences instead
of legacy ones. Here key is any ASCII key as described in legacy_text.
Additionally, all non text keypad keys will be reported as separate keys with `CSI u`
encoding, using dedicated numbers from the table below <functional>.

With this flag turned on, all key events that do not generate text are
represented in one of the following two forms:

```
CSI number; modifier u
CSI 1; modifier [~ABCDEFHPQS]
```

This makes it very easy to parse key events in an application. In particular,
ctrl+c will no longer generate the `SIGINT` signal, but instead be
delivered as a `CSI u` escape code. This has the nice side effect of making it
much easier to integrate into the application event loop. The only exceptions
are the Enter, Tab and Backspace keys which still generate the same
bytes as in legacy mode this is to allow the user to type and execute commands
in the shell such as `reset` after a program that sets this mode crashes
without clearing it. Note that the Lock modifiers are not reported for text
producing keys, to keep them usable in legacy programs. To get lock modifiers
for all keys use the report_all_keys enhancement.

### Report event types

This progressive enhancement (`0b10`) causes the terminal to report key repeat
and key release events. Normally only key press events are reported and key
repeat events are treated as key press events. See event_types for
details on how these are reported.

> [!NOTE]
> The Enter, Tab and Backspace keys will not have release
> events unless report_all_keys is also set, so that the user can still
> type reset at a shell prompt when a program that sets this mode ends without
> resetting it.

### Report alternate keys

This progressive enhancement (`0b100`) causes the terminal to report
alternate key values *in addition* to the main value, to aid in shortcut
matching. See key_codes for details on how these are reported. Note that
this flag is a pure enhancement to the form of the escape code used to
represent key events, only key events represented as escape codes due to the
other enhancements in effect will be affected by this enhancement. In other
words, only if a key event was already going to be represented as an escape
code due to one of the other enhancements will this enhancement affect it.

### Report all keys as escape codes

Key events that generate text, such as plain key presses without modifiers,
result in just the text being sent, in the legacy protocol. There is no way to
be notified of key repeat/release events. These types of events are needed for
some applications, such as games (think of movement using the `WASD` keys).

This progressive enhancement (`0b1000`) turns on key reporting even for key
events that generate text. When it is enabled, text will not be sent, instead
only key events are sent. If the text is needed as well, combine with the
Report associated text enhancement below.

Additionally, with this mode, events for pressing modifier keys are reported.
Note that *all* keys are reported as escape codes, including Enter,
Tab, Backspace etc. Note that this enhancement implies all keys
are automatically disambiguated as well, since they are represented in their
canonical escape code form.

### Report associated text

This progressive enhancement (`0b10000`) *additionally* causes key events that
generate text to be reported as `CSI u` escape codes with the text embedded
in the escape code. See text_as_codepoints above for details on the
mechanism. Note that this flag is an enhancement to report_all_keys
and is undefined if used without it.

## Detection of support for this protocol

An application can query the terminal for support of this protocol by sending
the escape code querying for the :ref:`current progressive enhancement
<progressive_enhancement>` status
followed by request for the `primary device attributes
<https://vt100.net/docs/vt510-rm/DA1.html>`__. If an answer for the device
attributes is received without getting back an answer for the progressive
enhancement the terminal does not support this protocol.

> [!NOTE]
> Terminal implementations of this protocol are **strongly** encouraged to
> implement all progressive enhancements. It does not make sense to
> implement only a subset. Nonetheless, there are likely to be some terminal
> implementations that do not do so, applications can detect such
> implementations by first setting the desired progressive enhancements and
> then querying for the current progressive enhancement <progressive_enhancement>

## Legacy key event encoding

In the default mode, the terminal uses a legacy encoding for key events. In
this encoding, only key press and repeat events are sent and there is no
way to distinguish between them. Text is sent directly as UTF-8 bytes.

Any key events not described in this section are sent using the standard
`CSI u` encoding. This includes keys that are not encodable in the legacy
encoding, thereby increasing the space of usable key combinations even without
progressive enhancement.

### Legacy functional keys

These keys are encoded using three schemes:

```
CSI number ; modifier ~
CSI 1 ; modifier {ABCDEFHPQS}
SS3 {ABCDEFHPQRS}
```

In the above, if there are no modifiers, the modifier parameter is omitted.
The modifier value is encoded as described in the modifiers section,
above, except that lock keys (such as Num lock and Caps lock)
are not encoded as the legacy mode has no encoding for them.

When the second form is used, the number is always `1` and must be
omitted if the modifiers field is also absent. The third form becomes the
second form when modifiers are present (`SS3 is the bytes 0x1b 0x4f`).

These sequences must match entries in the terminfo database for maximum
compatibility. The table below lists the key, its terminfo entry name and
the escape code used for it by kitty. A different terminal would use whatever
escape code is present in its terminfo database for the key.
Some keys have an alternate representation when the terminal is in *cursor key
mode* (the `smkx/rmkx` terminfo capabilities). This form is used only in
*cursor key mode* and only when no modifiers are present.

There are a few more functional keys that have special cased legacy encodings.
These are present because they are commonly used and for the sake of legacy
terminal applications that get confused when seeing CSI u escape codes:

Note that Backspace and ctrl+Backspace are swapped in some
terminals, this can be detected using the `kbs` terminfo property that
must correspond to the Backspace key.

All keypad keys are reported as their equivalent non-keypad keys. To
distinguish these, use the disambiguate <disambiguate> flag.

Terminals may choose what they want to do about functional keys that have no
legacy encoding. kitty chooses to encode these using `CSI u` encoding even in
legacy mode, so that they become usable even in programs that do not
understand the full kitty keyboard protocol. However, terminals may instead choose to
ignore such keys in legacy mode instead, or have an option to control this behavior.

### Legacy text keys

For legacy compatibility, the keys a-z 0-9
\` - = [ ] \\ ; '
, . / with the modifiers shift, alt,
ctrl, shift+alt, ctrl+alt are output using the following
algorithm:

1. If the alt key is pressed output the byte for `ESC (0x1b)`
1. If the ctrl modifier is pressed map the key using the table
   in ctrl_mapping.
1. Otherwise, if the shift modifier is pressed, output the shifted key,
   for example, `A` for `a` and `$` for `4`.
1. Otherwise, output the key unmodified

Additionally, ctrl+space is output as the NULL byte `(0x0)`.

Any other combination of modifiers with these keys is output as the appropriate
`CSI u` escape code.

> [!NOTE]
> Many of the legacy escape codes are ambiguous with multiple different key
> presses yielding the same escape code(s), for example, ctrl+i is the
> same as tab, ctrl+m is the same as Enter, ctrl+r
> is the same ctrl+shift+r, etc. To resolve these use the
> disambiguate progressive enhancement <disambiguate>.

## Functional key definitions

All numbers are in the Unicode Private Use Area (`57344 - 63743`) except
for a handful of keys that use numbers under 32 and 127 (C0 control codes) for legacy
compatibility reasons.

> [!NOTE]
> The escape codes above of the form `CSI 1 letter` will omit the
> `1` if there are no modifiers, since `1` is the default value.

> [!NOTE]
> The original version of this specification allowed F3 to be encoded as both
> CSI R and CSI ~. However, CSI R conflicts with the Cursor Position Report,
> so it was removed.

## Legacy ctrl mapping of ASCII keys

When the ctrl key and another key are pressed on the keyboard, terminals
map the result *for some keys* to a *C0 control code* i.e. an value from ``0 -
31``. This mapping was historically dependent on the layout of hardware
terminal keyboards and is not specified anywhere, completely. The best known
reference is [Table 3-5 in the VT-100 docs](https://vt100.net/docs/vt100-ug/chapter3.html).

The table below provides a mapping that is a commonly used superset of the table above.
Any ASCII keys not in the table must be left untouched by ctrl.

## Bugs in fixterms

The following is a list of errata in the `original fixterms proposal
<http://www.leonerd.org.uk/hacks/fixterms/>`_, corrected in this
specification.

- No way to disambiguate Esc key presses, other than using 8-bit controls
  which are undesirable for other reasons

- Incorrectly claims special keys are sometimes encoded using `CSI letter` encodings when it
  is actually `SS3 letter` in all terminals newer than a VT-52, which is
  pretty much everything.

- ctrl+shift+tab should be `CSI 9 ; 6 u` not `CSI 1 ; 5 Z`
  (shift+tab is not a separate key from tab)

- No support for the super modifier.

- Makes no mention of cursor key mode and how it changes encodings

- Incorrectly encoding shifted keys when shift modifier is used, for instance,
  for ctrl+shift+i is encoded as ctrl+I.

- No way to have non-conflicting escape codes for alt+letter,
  ctrl+letter, ctrl+alt+letter key presses

- No way to specify both shifted and unshifted keys for robust shortcut
  matching (think matching ctrl+shift+equal and ctrl+plus)

- No way to specify alternate layout key. This is useful for keyboard layouts
  such as Cyrillic where you want the shortcut ctrl+c to work when
  pressing the ctrl+С on the keyboard.

- No way to report repeat and release key events, only key press events

- No way to report key events for presses that generate text, useful for
  gaming. Think of using the WASD keys to control movement.

- Only a small subset of all possible functional keys are assigned numbers.

- Claims the `CSI u` escape code has no fixed meaning, but has been used for
  decades as `SCORC` for instance by xterm and ansi.sys and `DECSMBV
  <https://vt100.net/docs/vt510-rm/DECSMBV.html>`_ by the VT-510 hardware
  terminal. This doesn't really matter since these uses are for communication
  to the terminal not from the terminal.

- Handwaves that ctrl *tends to* mask with `0x1f`. In actual fact it
  does this only for some keys. The action of ctrl is not specified and
  varies between terminals, historically because of different keyboard layouts.

## Why xterm's modifyOtherKeys should not be used

- Does not support release events

- Does not fix the issue of Esc key presses not being distinguishable from
  escape codes.

- Does not fix the issue of some keypresses generating identical bytes and thus
  being indistinguishable

- There is no robust way to query it or manage its state from a program running
  in the terminal.

- No support for shifted keys.

- No support for alternate keyboard layouts.

- No support for modifiers beyond the basic four.

- No support for lock keys like Num lock and Caps lock.

- Is completely unspecified. The most discussion of it available anywhere is
  [here](https://invisible-island.net/xterm/modified-keys.html)
  And it contains no specification of what numbers to assign to what function
  keys beyond running a Perl script on an X11 system!!
