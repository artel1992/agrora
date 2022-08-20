<template>
  <div>
    edit form
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

const props = defineProps<{ form: SliderProps }>()
const emits = defineEmits(['update:form', 'save', 'close'])
const innerForm = ref<SliderProps>()
onMounted(() => {
  innerForm.value = props.form
})
const changeImages = (v: any, ind: number) => {
  const images = innerForm.value ? innerForm.value?.images : null
  if (!images)
    return
  images[ind] = v.target.value
}
const save = () => {
  emits('update:form', innerForm.value)
}
</script>

<style scoped>

</style>