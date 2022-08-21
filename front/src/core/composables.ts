import {useCMSStore} from "@/store/cms";
import {computed, onMounted, Ref, ref, watch, getCurrentInstance} from "vue";
import {EditableComponent, EditableComponentProps, EditFormProps} from "@/core/interfaces";
import {storeToRefs} from "pinia";
import {$vfm} from "vue-final-modal";

interface EditableComponentContext<T> {
    form: Ref<T | undefined>,
    classes: Ref<EditableComponent<T>['structure']['classes']>
    modalEditOpen: Ref<boolean>
    modalEditName: Ref<string>
    modalConfName: Ref<string>
    modalConfOpen: Ref<boolean>
    saveForm: (savedForm: T) => void
    closeEditForm: (defaultForm: T) => void
}

export function useEditableComponent<T = any>(modalEdit: string, modalConf: string, props: Readonly<EditableComponentProps<T>>, emits: any): EditableComponentContext<T> {
    const {nowEdit} = storeToRefs(useCMSStore())
    const {setNowEdit} = useCMSStore()
    const modalEditOpen = ref(false)
    const modalEditName = ref(modalEdit)
    const modalConfName = ref(modalConf)
    const modalConfOpen = ref(false)
    const form = ref<T>()
    const classes = ref<EditableComponent<T>['structure']['classes']>({})
    watch(nowEdit, (value) => {
        if (value && value.id === props.component.id)
            $vfm.show(modalEditName.value)
        if (value === null)
            $vfm.hide(modalEditName.value)
    })
    watch((): boolean => props.modalEdit, (value) => {
        modalEditOpen.value = value
    })
    watch((): boolean => props.modalConf, (value) => {
        modalConfOpen.value = value
    })
    onMounted(() => {
        if (props.component) {
            form.value = props.component.structure.props
            classes.value = props.component.structure.classes
        }
        const component = getCurrentInstance()
        modalEditName.value += component ? `-${component.uid}` : ''
        modalConfName.value += component ? `-${component.uid}` : ''
    })
    const closeEditForm = (defaultForm: T) => {
        form.value = defaultForm
        setNowEdit(null)
    }
    const changeClass = (className: string) => {
        // form.value.classes = {}
    }
    const saveForm = (savedForm: T) => {
        const {component} = props
        closeEditForm(savedForm)
        emits('update:component', {
            ...component,
            structure: {...component.structure, props: savedForm}
        } as EditableComponent<T>)
    }
    return {
        modalEditOpen,
        form,
        modalEditName,
        modalConfName,
        modalConfOpen,
        classes,
        saveForm,
        closeEditForm
    }
}

export function useEditForm<T = any>(props: Readonly<EditFormProps<T>>, emits: any) {
    const innerForm = ref<T>()
    const defaultForm = JSON.stringify(props.form)
    const isChanged = computed(() => defaultForm !== JSON.stringify(innerForm.value))
    onMounted(() => {
        innerForm.value = props.form
    })
    const save = () => {
        emits('save', innerForm.value)
    }
    const close = () => {
        innerForm.value = JSON.parse(defaultForm)
        save()
    }
    return {
        innerForm,
        defaultForm,
        isChanged,
        save,
        close
    }
}


