<template>
  <div>
    edit form
    <button @click="save">Save</button>
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

const props = defineProps<{ form: TopProductsProps }>()
const emits = defineEmits(['update:form', 'save', 'close'])
const innerForm = ref<TopProductsProps>()
onMounted(() => {
  innerForm.value = props.form
})
const save = () => {
  emits('update:form', innerForm.value)
}
</script>

<style scoped>

</style>