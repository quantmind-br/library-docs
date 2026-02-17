---
title: Moodle App Coding style | Moodle Developer Resources
url: https://moodledev.io/general/development/policies/codingstyle-moodleapp
source: sitemap
fetched_at: 2026-02-17T15:58:59.353899-03:00
rendered_js: false
word_count: 1068
summary: This document outlines specific coding style guidelines and exceptions for the Moodle App, focusing on TypeScript and Angular best practices to ensure code consistency and readability.
tags:
    - moodle-app
    - typescript
    - coding-standards
    - eslint
    - angular
    - development-guidelines
category: guide
---

This document outlines the exceptions to the [Coding style](https://moodledev.io/general/development/policies/codingstyle) and [JavaScript Coding Style](https://docs.moodle.org/dev/JavaScript_Coding_Style) which apply to the Moodle App and also includes rules for other technologies that are used in the app, like Typescript and Angular.

Unless otherwise specified, developers should follow the indications included on those documents.

Most rules are enforced with [ESLint](https://github.com/typescript-eslint/typescript-eslint) and won't be mentioned in this document, make sure to integrate a linter in your development environment.

## Goals[​](#goals "Direct link to Goals")

Consistent coding style is important in any development project, and particularly when many developers are involved. A standard style helps to ensure that the code is easier to read and understand, which helps overall quality.

Abstract goals we strive for:

- simplicity
- readability
- tool friendliness

Note that much of the existing code may not follow all of these guidelines — we continue to upgrade this code when we see it.

## TypeScript[​](#typescript "Direct link to TypeScript")

### Disabling ESLint rules[​](#disabling-eslint-rules "Direct link to Disabling ESLint rules")

In some situations, it may be necessary to [disable ESLint rules using inline comments](https://eslint.org/docs/user-guide/configuring/rules#disabling-rules). Although this is discouraged, it is allowed on certain use-cases.

Most of the time, however, this could be solved by refactoring code. So think twice before disabling a rule.

Warnings should be treated with the same severity as errors, even if they are allowed by the linter. The reasoning behind this is that warnings are useful when new rules are introduced that affect existing code, but new code should always conform to the rules or explicitly disable them.

### Using async / await[​](#using-async--await "Direct link to Using async / await")

Using async/await is encouraged, but it shouldn't be mixed with .then/.catch/.finally. Using both can make code difficult to understand. As a rule of thumb, there should only be one style in a given function.

Good

```
asyncfunctiongreet(){
const response =awaitfetch('/profile.json');
const data =await response.json();

alert(`Hello, ${data.name}!`);
}
```

Allowed, but discouraged

```
functiongreet(){
returnfetch('/profile.json')
.then(response => response.json())
.then(data =>{
alert(`Hello, ${data.name}!`);
});
}
```

Bad

```
asyncfunctiongreet(){
const response =awaitfetch('/profile.json');

return response.json().then(data =>{
alert(`Hello, ${data.name}!`);
});
}
```

Async/await is [syntactic sugar](https://en.wikipedia.org/wiki/Syntactic_sugar) for Promises, so it should always be possible to avoid using .then/.catch/.finally.

To prevent making asynchronous operations difficult to spot, using await should be limited to simple statements such as one liners, assignments and if guards with a single condition.

### If guards[​](#if-guards "Direct link to If guards")

Using if guards is encouraged to reduce indentation levels. They should handle edge cases and leave the main indentation level for normal code.

More concretely, when an if block contains a non-conditional ending statement, it should not chain other blocks.

Good

```
getPrivateInfo(){
if(!this.isLoggedIn()){
thrownewError('Please, log in!');
}

returnthis.privateInfo;
}
```

Bad

```
getPrivateInfo(){
if(!this.isLoggedIn()){
thrownewError('Please, log in!');
}else{
returnthis.privateInfo;
}
}
```

### Avoid abusing user-defined type guards[​](#avoid-abusing-user-defined-type-guards "Direct link to Avoid abusing user-defined type guards")

User-defined type guards are an advanced TypeScript feature that can be very useful for working in heavily typed applications. However, they can also be confusing for newcomers, so they should only be used when they are really necessary.

Good

```
functionhasSecret(user: User): user is{ secret:string}{
return'secret'in user;
}

functiongetSecret(user: User){
if(!hasSecret(user)){
thrownewError("This user doesn't have a secret");
}

return user.secret;
}
```

An alternative to defining type guards is to use built-in operations to perform type checks. For example, the following code would also take advantage of TypeScript inference:

Good

```
interfaceUser{
    secret:string;
}

interfacePost{
    title:string;
}

functiongetSecret(object: User | Post){
if('secret'in object){
thrownewError("This object doesn't have a secret");
}

return object.secret;
}
```

In some situations, the only solution is to use type assertions. Although this approach is simpler to understand and more straightforward, it is dangerous because we lose inference checks:

Allowed, but discouraged

```
functionhasSecret(user: User):boolean{
return'secret'in user;
}

functiongetSecret(user: User){
if(!hasSecret(user)){
thrownewError("This user doesn't have a secret");
}

const userWithSecret = user as{ secret:string};

return userWithSecret.secret;
}
```

### Spread operator[​](#spread-operator "Direct link to Spread operator")

The spread operator is allowed, but it's recommended to include a comment explaining what it is doing to make the code easier to understand. You can also replace it for simpler alternatives.

Good

```
const numbers =[4,5,6];
const properties ={ surname:'Doe'};

console.log([1,2,3].concat(numbers));
console.log(Object.assign({ name:'Mary'}, properties));
console.log(Math.max.apply(Math, numbers));
```

Good

```
const numbers =[4,5,6];
const properties ={ surname:'Doe'};

console.log([1,2,3,...numbers]);// Concatenate numbers.
// Create a new object including all properties and a new one.
console.log({ name:'Mary',...properties });
console.log(Math.max(...numbers));// Find max number in array.
```

### String interpolation[​](#string-interpolation "Direct link to String interpolation")

It is encouraged to use string interpolation using backticks if it makes the code more readable.

Good

```
functiongreet(name:string){
alert(`Hello, ${name}!`);
}
```

Allowed, but discouraged

```
functiongreet(name:string){
alert('Hello, '+ name +'!');
}
```

### Avoid declaring variables using commas[​](#avoid-declaring-variables-using-commas "Direct link to Avoid declaring variables using commas")

In order to have cleaner diffs, it is not allowed to declare variables using commas. This also results in a better alignment of variable names, making the code more readable.

Good

```
const foo ='foo';
const bar ='bar';
```

Bad

```
const foo ='foo',
      bar ='bar';
```

### Avoiding having too many optional arguments[​](#avoiding-having-too-many-optional-arguments "Direct link to Avoiding having too many optional arguments")

In some situations, functions end up having a lot of optional arguments and this results in unreadable code and a cumbersome developer experience (having to pass multiple null or undefined values).

When these situations arise, a good approach to solve it is using an options object instead.

As a rule of thumb, when a method has more than two optional arguments that are not required to be used together, use an options object (better naming can be used for each particular scenario).

Good

```
interfaceHelloOptions{
    surname?:string;
    emphasis?:string;
    times?:number;
}

functionsayHello(name:string,{ surname, emphasis, times }: HelloOptions){
    surname = surname ??'';
    emphasis = emphasis ??'!';
    times = times ??1;

const fullname =`${name}${surname}`.trim();

for(let i =0; i < times; i++){
console.log(`Hello ${fullname}${emphasis}`);
}
}

sayHello('World',{ times:3});
```

Bad

```
functionsayHello(
    name:string,
    surname:string='',
    emphasis:string='!',
    times:number=1,
){
const fullname =`${name}${surname}`.trim();

for(let i =0; i < times; i++){
console.log(`Hello ${fullname}${emphasis}`);
}
}

sayHello('World',undefined,undefined,3);
```

### Using declaration files[​](#using-declaration-files "Direct link to Using declaration files")

[Declaration files](https://www.typescriptlang.org/docs/handbook/declaration-files/introduction.html) can be very useful in TypeScript and it is encouraged to use them when appropriate. But it's not recommended to abuse them either, here's some situations when it may be a good idea to use them:

- Declaring types for external dependencies — Libraries that don't include their own declarations and are missing from [DefinitelyTyped](https://github.com/DefinitelyTyped/DefinitelyTyped) (the packages you find under `@types/` in npm).
- Global declarations and extensions — Any variable you add to the window object can be declared by extending the `Window` interface. The same idea applies for extending external dependencies.
- Local declarations — Sometimes, it may be useful to create a dedicated declaration file when source files are growing too large. But this technique should not be used to substitute proper code organisation.

### Using constants[​](#using-constants "Direct link to Using constants")

In order to optimize [Code Splitting](https://webpack.js.org/guides/code-splitting/), constants that are exported should be declared in [a constants file](https://moodledev.io/general/app/development/development-guide#constants-files):

Good

```
// src/core/features/my-feature/constants.ts
exportconstMY_SERVICE_NAME='...';

// src/core/features/my-feature/services/my-service.ts
import{MY_SERVICE_NAME}from'../constants';

exportclassMyServiceimplementsNamedService{

    name =MY_SERVICE_NAME;

}
```

Bad

```
// src/core/features/my-feature/services/my-service.ts
exportclassMyServiceimplementsNamedService{

publicstaticreadonlyMY_SERVICE_NAME='...';

    name = MyService.MY_SERVICE_NAME;

}
```

Bad

```
// src/core/features/my-feature/services/my-service.ts
exportconstMY_SERVICE_NAME='...';

exportclassMyServiceimplementsNamedService{

    name =MY_SERVICE_NAME;

}
```

In contrast, constants that are private or protected should be declared as static readonly class properties. Also, avoid calling them using `this.CONSTANT` form (given that they are static members):

Good

```
exportclassMyService{

protectedstaticreadonlyMY_CONSTANT='...';

publicsomeMethod():void{
alert(MyService.MY_CONSTANT);
}

}
```

Bad

```
constMY_CONSTANT='...';

exportclassMyService{

publicsomeMethod():void{
alert(MY_CONSTANT);
}

}
```

Bad

```
exportclassMyService{

protectedstaticreadonlyMY_CONSTANT='...';

publicsomeMethod():void{
alert(this.MY_CONSTANT);
}

}
```

If a constant needs to be used in a component template, it should be declared in the component without "static" because static properties cannot be used in templates. Please notice that the naming convention for non-static properties is camelCase.

Good

```
exportclassMyComponent{

protectedreadonly myConstant ='...';

}
```

Bad

```

exportclassMyComponent{

protectedreadonlyMY_CONSTANT='...';

}
```

### Angular Signals[​](#angular-signals "Direct link to Angular Signals")

All signals in class properties must be defined as readonly properties to avoid overriding the whole signal by mistake. This includes input signals, computed signals, etc.

Good

```
exportclassMyComponent{

protectedreadonly myInput =input('...');
protectedreadonly mySignal =signal('...');
protectedreadonly myComputed =computed(()=>...);

}
```

Bad

```

exportclassMyComponent{

protected myInput =input('...');
protected mySignal =signal('...');
protected myComputed =computed(()=>...);

}
```

## Angular[​](#angular "Direct link to Angular")

### Avoid calling methods in templates[​](#avoid-calling-methods-in-templates "Direct link to Avoid calling methods in templates")

Method calls should be avoided in template rendering, including structural directives like `ngIf` or `ngFor`. The same applies to the new control flow syntax with `@if` or `@for`.

Angular templates can be rendered very often, and calling methods on every render could cause some unintended performance issues. For that reason, it is usually safer to rely on values rather than methods.

In some situations, a simple method that only returns a value would be acceptable, but it opens the door to become an issue if the method is refactored to do something more complicated. That's why it is discouraged to use methods altogether.

Good

```
@if (isAdmin) {
<div><!-- Show admin content --></div>
}
```

Allowed, but discouraged

```
@if (site.isAdmin()) {
<div><!-- Show admin content --></div>
}
```

Of course, this doesn't mean that you can't use any methods on a template. Not every method used on a template is called in every render.

For example, using methods in event handlers is fine:

Good

```
<button(click)="login()">
    Login
</button>
```

#### A warning about using getters[​](#a-warning-about-using-getters "Direct link to A warning about using getters")

Other frameworks have patterns to solve this problem, for example Vue has [Computed Properties](https://vuejs.org/guide/essentials/computed.html#computed-properties) and React has the [useMemo hook](https://reactjs.org/docs/hooks-reference.html#usememo).

However, Angular doesn't include a built-in pattern for these situations, so these properties should be managed as part of the logic for the component.

Be careful when using getters, which may give the wrong impression that a method is not being called:

Allowed, but discouraged

```
get isAdmin(): boolean {
    return this.site.isAdmin();
}
```

Even if this looks like using a property in the template, it is still calling a method in every render.

### Maximise the number of attributes per line[​](#maximise-the-number-of-attributes-per-line "Direct link to Maximise the number of attributes per line")

There is a maximum line length of 140 characters for templates. Whenever that length is surpassed, the attributes should be distributed in multiple lines trying to reduce the number of total lines, instead of dedicating one line per attribute.

Good

```
@for (course of courses; track course.id) {
<ion-item
[title]="course.title"
[class.selected]="isSelected(course)"class="ion-text-wrap"
buttondetail="true"
(click)="selectCourse(course)">
<ion-label>
            {{ course.title }}
</ion-label>
</ion-item>
}
```

Bad

```
@for (course of courses; track course.id) {
<ion-item
[title]="course.title"
[class.selected]="isSelected(course)"
class="ion-text-wrap"
button
detail="true"
(click)="selectCourse(course)">
<ion-label>
            {{ course.title }}
</ion-label>
</ion-item>
}
```

### Declaring page modules[​](#declaring-page-modules "Direct link to Declaring page modules")

When creating a page component, it should be declared as a standalone component and exported as default class so it can be easily [lazy loaded](https://moodledev.io/general/app/development/development-guide#routing).

Good

```
// file: core/features/feature/pages/index/index.ts
@Component({
    selector:'page-core-feature-index',
    templateUrl:'index.html',
    imports:[
        CoreSharedModule,
],
})
exportdefaultclassCoreFeatureIndexPageComponent{}
```

```
// file: core/features/feature/feature.module.ts
const routes: Routes =[
{
        path:'feature',
loadComponent:()=>import('./pages/index/index'),
},
];
```

Bad

```
// file: core/features/feature/pages/index/index.page.ts
@Component({
    selector:'page-core-feature-index',
    templateUrl:'index.html',
    standalone:false,
})
exportclassCoreFeatureIndexPageComponent{}
```

```
// file: core/features/feature/pages/index/index.module.ts
const routes: Routes =[
{
        path:'',
        component: CoreFeatureIndexPageComponent,
},
];

@NgModule({
    imports:[
        RouterModule.forChild(routes),
        CoreSharedModule,
],
    declarations:[
        CoreFeatureIndexPageComponent,
],
})
exportclassCoreFeatureIndexPageModule{}
```