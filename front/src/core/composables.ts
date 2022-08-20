import {useCMSStore} from "@/store/cms";
import {computed, onMounted, ref, watch} from "vue";
import {EditableComponent, EditableComponentProps, EditFormProps} from "@/core/interfaces";
import {storeToRefs} from "pinia";
import {$vfm} from "vue-final-modal";
import {SliderProps} from "@/core/interfaces/props/slider";


export function useEditableComponent<T = any>(modal: string, props: Readonly<EditableComponentProps<T>>, emits: any): any {
    const {nowEdit} = storeToRefs(useCMSStore())
    const {setNowEdit} = useCMSStore()
    const modalOpen = ref(false)
    const modalName = ref(modal)
    const form = ref<T>()
    watch(nowEdit, (value) => {
        if (value && value.id === props.component.id)
            $vfm.show(modalName.value)
        if (value === null)
            $vfm.hide(modalName.value)
    })
    onMounted(() => {
        form.value = props.component.structure.props
    })
    const closeEditForm = (defaultForm: EditableComponent<T>['structure']['props']) => {
        form.value = defaultForm
        setNowEdit(null)
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
        modalOpen,
        form,
        modalName,
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


