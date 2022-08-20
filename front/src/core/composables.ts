import {useCMSStore} from "@/store/cms";
import {ref, watch} from "vue";
import {EditableComponent, EditableComponentProps} from "@/core/interfaces";
import {storeToRefs} from "pinia";
import {$vfm} from "vue-final-modal";


export function useEditableComponent<T = any>(modal: string, props: Readonly<EditableComponentProps<T>>): any {
    const {nowEdit} = storeToRefs(useCMSStore())
    const {setNowEdit} = useCMSStore()
    const modalOpen = ref(false)
    const modalName = ref(modal)
    const form = ref()
    watch(nowEdit, (value) => {
        if (value && value.id === props.component.id)
            $vfm.show(modalName.value)
        if (value === null)
            $vfm.hide(modalName.value)
    })
    const closeEditForm = (
        defaultForm: EditableComponent<T>['structure']['props']
    ) => {
        form.value = defaultForm
        setNowEdit(null)
    }
    return {
        modalOpen,
        form,
        modalName,
        closeEditForm
    }
}


