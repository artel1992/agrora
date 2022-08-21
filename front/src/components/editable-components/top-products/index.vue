<template>
  <div class="flex justify-center flex-wrap space-y-3 items-center w-full overflow-hidden space-x-3" v-if="form">
    <div class="min-h-40 bg-rose-50 text-red-400 w-full text-center" v-if="form.products.length===0">
      Empty
    </div>
    <div
        v-for="(product,ind) in form.products" :key="ind"
        class="p-6 bg-white rounded-xl shadow-xl hover:shadow-2xl transition-all transform duration-500">
      <img class="w-64 object-cover rounded-t-md object-cover h-64" :src="product.img"
           alt=""/>
      <div class="mt-4">
        <h1 class="text-2xl font-bold text-gray-700">{{ product.title }}</h1>
        <p class="text-sm mt-2 text-gray-700">{{ product.subtitle }}</p>
        <div class="mt-3 space-x-4 flex p-1">
          <div
              class="p-1 border-4 rounded-full cursor-pointer hover:border-green-200 hover:scale-105 transition transform duration-200">
            <span class="block h-6 w-6 bg-green-400 rounded-full"> </span>
          </div>
          <div
              class="p-1 border-4 rounded-full cursor-pointer hover:border-blue-200 hover:scale-105 transition transform duration-200">
            <span class="block h-6 w-6 bg-blue-400 rounded-full"> </span>
          </div>
          <div
              class="p-1 border-4 rounded-full cursor-pointer hover:border-yellow-200 hover:scale-105 transition transform duration-200">
            <span class="block h-6 w-6 bg-yellow-400 rounded-full"> </span>
          </div>
        </div>
        <div class="mt-4 mb-2 flex justify-between pl-4 pr-2">
          <button class="block text-xl font-semibold text-gray-700 cursor-auto">{{ product.price }}</button>
          <button
              class="text-lg block font-semibold py-2 px-6 text-green-100 hover:text-white bg-green-400 rounded-lg shadow hover:shadow-md transition duration-300">
            Buy
          </button>
        </div>
      </div>
    </div>
  </div>

  <vue-final-modal :name="modalEditName"
                   v-model="modalEditOpen"
                   :click-to-close="false"
                   :min-width="0"
                   :min-height="0"
                   classes="flex justify-center items-center"
                   :max-height="100">
    <edit-form v-if="form" @save="saveForm"
               :form="form"></edit-form>
  </vue-final-modal>
  <vue-final-modal :name="modalConfName"
                   v-model="modalConfOpen"
                   :click-to-close="false"
                   :min-width="0"
                   :min-height="0"
                   classes="flex justify-center items-center"
                   :max-height="100">
    <template #default="{close}">
      <config-form v-if="component"
                   :title="component.title"
                   @update:title="(title)=>$emit('update:component',{...component,title})"
                   :classes="classes"

                   @update:classes="(cls)=>changeClasses(cls,close)"
      ></config-form>
    </template>
  </vue-final-modal>
</template>

<script lang="ts">
export default {
  name: "TopProducts"
}
</script>
<script setup lang="ts">
import EditForm from "@/components/editable-components/top-products/EditForm.vue";
import ConfigForm from "@/components/editable-components/top-products/ConfigForm.vue";
import {defineEmits, defineProps} from "vue";
import {EditableComponent} from "@/core/interfaces";
import {TopProductsProps} from "@/core/interfaces/props/top-products";
import {useEditableComponent} from "@/core/composables";

const props = defineProps<{ component: EditableComponent<TopProductsProps>, modalEdit: boolean, modalConf: boolean }>()
const emits = defineEmits<{
  (eventName: 'update:component', form: EditableComponent<TopProductsProps>): void
}>()
const {
  modalEditName,
  saveForm,
  modalEditOpen,
  modalConfName,
  modalConfOpen,
  form,
  classes
} = useEditableComponent<TopProductsProps>('edit-top-products', 'conf-top-products', props, emits)
const changeClasses = (newClasses: EditableComponent<TopProductsProps>['structure']['classes'], cb: CallableFunction) => {
  classes.value = newClasses
  modalConfOpen.value = false
  emits('update:component', {...props.component, structure: {...props.component.structure, classes: classes.value}})
  cb()
}
</script>
<style scoped>

</style>