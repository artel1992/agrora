<template>
  <div class="bg-white p-4 space-y-2" style="width: 1000px" v-if="innerForm">
    <div>
      <i class='bx bx-plus px-2 py-1 bg-green-300 rounded-md text-green-800 shadow hover:shadow-md cursor-pointer'
         @click="innerForm.products.push({})"></i>
    </div>
    <div class="space-y-3 max-h-[85vh] overflow-auto">
      <div v-for="(product,ind) in innerForm.products " :key="ind">
        <div class="flex items-start justify-center space-x-3">
          <img :src="product.img" class="w-40 h-40 rounded object-cover" alt=""/>
          <div class="space-y-3">
            <input v-model="innerForm.products[ind].img" class="w-full border border-zinc-400 rounded-l-lg px-1"/>
            <input v-model="innerForm.products[ind].title" class="w-full border border-zinc-400 rounded-l-lg px-1"/>
            <input v-model="innerForm.products[ind].subtitle" class="w-full border border-zinc-400 rounded-l-lg px-1"/>
            <input v-model="innerForm.products[ind].price" class="w-full border border-zinc-400 rounded-l-lg px-1"/>
          </div>
        </div>
      </div>
    </div>
    <div class="space-x-3">
      <button @click="save"
              :disabled="!isChanged"
              class="bg-green-500 px-2 py-1 text-white rounded-md shadow-md hover:shadow-xl font-light transition-shadow  ease-in duration-200  disabled:bg-zinc-400 disabled:text-zinc-300 disabled:hover:shadow-md">
        Save
      </button>
      <button @click="close"
              class="bg-rose-500 px-2 py-1 text-white rounded-md  shadow-md hover:shadow-xl font-light transition-shadow">
        Cancel
      </button>
    </div>
  </div>
</template>

<script lang="ts">
export default {
  name: "EditForm"
}
</script>
<script setup lang="ts">
import {defineProps, defineEmits, ref, onMounted} from "vue";
import {SliderProps} from "@/core/interfaces/props/slider";
import {TopProductsProps} from "@/core/interfaces/props/top-products";
import {useEditForm} from "@/core/composables";

const props = defineProps<{ form: TopProductsProps }>()
const emits = defineEmits(['save'])

const {
  innerForm,
  defaultForm,
  isChanged,
  save,
  close
} = useEditForm<TopProductsProps>(props, emits)
</script>

<style scoped>

</style>