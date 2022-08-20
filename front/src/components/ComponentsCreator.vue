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
        <div v-for="(child,i) in modelValue.children" :key="child.name">
          <components-creator :model-value="modelValue.children[i]"
                              @update:modelValue="emits('update:modelValue',modelValue)"></components-creator>
        </div>
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
import {defineEmits, defineProps, ref} from "vue";
import EditToolbarComponent from "@/components/editable-components/EditToolbarComponent.vue";
import {EditableComponent} from "@/core/interfaces";
import {useCMSStore} from "@/store/cms";

const {setNowEdit, saveEditableComponent, deleteEditableComponent} = useCMSStore()
const hover = ref(false)
const props = defineProps<{ modelValue: EditableComponent<any> }>()
const emits = defineEmits<{
  (eventName: 'update:modelValue', value: EditableComponent<any>): void
}>()
const onEdit = () => {
  setNowEdit(props.modelValue)
}
const save = () => {
  saveEditableComponent(props.modelValue)
}
const deleteComponent = () => {
  deleteEditableComponent(props.modelValue.id)
}
</script>
<style scoped>
.active {
  @apply ring-1 ring-blue-300;
}
</style>