<template>
  <div
      class="relative" ref="container"
      @mouseenter="showMe" @mouseleave="hover=false">
    <transition name="fade">
      <edit-toolbar-component v-if="hover" @edit="onEdit" @save="save" @config="modalConf=true"
                              @delete="deleteComponent"></edit-toolbar-component>
    </transition>
    <div :class="modelValue.structure.classes">
      <component :is="modelValue.name"
                 :component="modelValue" :modal-conf="modalConf" :modal-edit="modalEdit"
                 @update:component="(comp)=>$emit('update:modelValue',comp)"
                 class="relative component">
        <template v-if="modelValue.children.length > 0">
          <draggable
              @end="endDrag"
              v-model="component.children"
              v-if="component"
              item-key="name"
              handle=".bx-move"
          >
            <template #item="{ element,index }">
              <div>
                <components-creator :model-value="element"
                                    @update:model-value="(comp)=>updateChild(comp,index)"></components-creator>
              </div>
            </template>
          </draggable>
        </template>
      </component>
    </div>

    <div class="text-center text-blue-500 cursor-pointer transition-[max-height] duration-500 transition-opacity
    hover:opacity-100 hover:max-h-screen
    overflow-hidden max-h-2 opacity-0"
         v-if="component && component.structure.config&& component.structure.config.has_children">
      <i class='bx bxs-layer-plus block' @click="loadEmptyComponents"></i>
      <div v-for="comp in emptyComponents" :key="comp.name" @click="addComponents(comp)">
        {{ comp.name }}
      </div>
    </div>
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

const container = ref(null)
const {setNowEdit, saveEditableComponent, deleteEditableComponent, createComponent, getEmptyComponents} = useCMSStore()
const hover = ref(false)
const props = defineProps<{ modelValue: EditableComponent<any> }>()
const emits = defineEmits<{
  (eventName: 'update:modelValue', value: EditableComponent<any>): void
}>()
const component = ref()
const emptyComponents = ref([])
onMounted(() => {
  component.value = props.modelValue
})
const modalEdit = ref(false)
const modalConf = ref(false)
const showMe = (ent: any) => {
  if (container.value === ent.target)
    ent.target.classList.add('active')
  hover.value = true
}
const onEdit = () => {
  setNowEdit(props.modelValue)
}
const save = () => {
  saveEditableComponent(props.modelValue)
}
const deleteComponent = () => {
  deleteEditableComponent(props.modelValue.id)
}
const loadEmptyComponents = async () => {
  emptyComponents.value = (await getEmptyComponents())
}
const addComponents = async (comp: EditableComponent<any>) => {
  component.value.children.push((await createComponent({...comp, parent: component.value.id})))

}
const updateChild = (newComp: EditableComponent<any>, ind: number) => {
  (component.value).children[ind] = newComp
  emits('update:modelValue', component.value)
}

function endDrag({newIndex, oldIndex}: { newIndex: number, oldIndex: number }) {
  component.value.children[newIndex].sequence_number = newIndex
  component.value.children[oldIndex].sequence_number = oldIndex
}
</script>
<style scoped>
.active {
  @apply ring-1 ring-blue-300;
}
</style>