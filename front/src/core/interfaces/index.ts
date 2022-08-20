import {ComponentPropsOptions} from "@vue/runtime-core";

declare type ClassType = { [key: string]: boolean } | string[]

export interface Structure<T> {
    classes: ClassType
    props: T
}

export interface EditableComponent<T> {
    id: number
    name: string
    parent?: number
    structure: Structure<T>
    path: string
    sequence_number: number
    children: EditableComponent<T>[]
}

export interface EditableComponentProps<T> {
    component: EditableComponent<T>
}

export interface EditFormProps<T> {
    form: EditableComponent<T>['structure']['props']
}