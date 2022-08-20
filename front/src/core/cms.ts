import {App, Component} from "vue";

export function registerComponents(app: App, components: Component[]): void {
    for (const component of components) {
        app.component(component.name as string, component)
    }
}