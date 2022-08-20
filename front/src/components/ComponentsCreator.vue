<template>
  <div class="relative" :class="{active:hover}" @mouseenter="hover=true" @mouseleave="hover=false">
    <transition name="fade">
      <edit-toolbar-component v-if="hover" @edit="onEdit" @save="save"></edit-toolbar-component>
    </transition>
    <component :is="modelValue.name" :class="modelValue.structure.classes"
               :component="modelValue"
               @update:component="emits('update:modelValue',modelValue)"
               class="relative">
      <template v-if="modelValue.children.length > 0">
        <draggable
            @end="log"
            v-model="component.children"
            v-if="component"
            item-key="name"
            handle=".bx-move"
        >
          <template #item="{ element }">
            <div>
              <components-creator :model-value="element"></components-creator>
            </div>
          </template>
        </draggable>
      </template>
    </component>
  </div>

</template>

<script lang="ts">
export default {
  name: "ComponentsCreator"
}
</script>
<script setup lang="ts">
import {defineEmits, defineProps, onMounted, ref} from "vue";
import {EditableComponent} from "@/core/interfaces";
import {useCMSStore} from "@/store/cms";
import draggable from "vuedraggable";
import EditToolbarComponent from "@/components/editable-components/EditToolbarComponent.vue";

const {setNowEdit, saveEditableComponent, deleteEditableComponent} = useCMSStore()
const hover = ref(false)
const props = defineProps<{ modelValue: EditableComponent<any> }>()
const emits = defineEmits<{
  (eventName: 'update:modelValue', value: EditableComponent<any>): void
}>()
const component = ref()
onMounted(() => {
  component.value = props.modelValue
})
const onEdit = () => {
  setNowEdit(props.modelValue)
}
const save = () => {
  saveEditableComponent(props.modelValue)
}
const deleteComponent = () => {
  deleteEditableComponent(props.modelValue.id)
}

function log({newIndex, oldIndex}) {
  component.value.children[newIndex].sequence_number = newIndex
  component.value.children[oldIndex].sequence_number = oldIndex
}
</script>
<style scoped>
.active {
  @apply ring-1 ring-blue-300;
}
</style>