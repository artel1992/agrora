<template>
  <div class="flex justify-center items-center w-full overflow-hidden space-x-3" v-if="component">
    <div
        v-for="(product,ind) in component.structure.props.products" :key="ind"
        class="p-6 bg-white rounded-xl shadow-xl hover:shadow-2xl transition-all transform duration-500">
      <img class="w-64 object-cover rounded-t-md" :src="product.img"
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
</template>

<script lang="ts">
export default {
  name: "TopProducts"
}
</script>
<script setup lang="ts">
import {defineProps} from "vue";
import {EditableComponent} from "@/core/interfaces";
import {TopProductsProps} from "@/core/interfaces/props/top-products";

const props = defineProps<{ component: EditableComponent<TopProductsProps> }>()
</script>
<style scoped>

</style>