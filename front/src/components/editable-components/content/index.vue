<template>
  <div v-if="form" v-html="form.content" ></div>
  <vue-final-modal :name="modalName"
                   v-model="modalOpen"
                   :click-to-close="false"
                   :min-width="0"
                   :min-height="0"
                   classes="flex justify-center items-center"
                   :max-width="1000">
    <edit-form v-if="form" @save="saveForm"
               :form="form"></edit-form>
  </vue-final-modal>
</template>

<script lang="ts">
export default {
  name: "ContentComponent"
}
</script>
<script setup lang="ts">
import {defineEmits, defineProps, ref} from "vue";
import {EditableComponent} from "@/core/interfaces";
import {useEditableComponent} from "@/core/composables";
import {ContentProps} from "@/core/interfaces/props/content";
import EditForm from "@/components/editable-components/content/EditForm.vue";

const props = defineProps<{ component: EditableComponent<ContentProps> }>()
const emits = defineEmits<{
  (eventName: 'update:component', form: EditableComponent<ContentProps>): void
}>()

const {
  modalName,
  modalOpen,
  form,
  saveForm
} = useEditableComponent<ContentProps>('edit-content', props, emits)
const currentImageIndex = ref(0)

</script>
<style>
@import "quill/dist/quill.core.css";
</style>