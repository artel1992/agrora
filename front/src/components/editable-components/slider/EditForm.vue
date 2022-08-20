<template>
  <div class="bg-white p-4 space-y-3" style="width: 1000px">
    <div>
      <i class='bx bx-plus px-2 py-1 bg-green-300 rounded-md text-green-800 shadow hover:shadow-md cursor-pointer'
         @click="innerForm.images.push('')"></i>
    </div>
    <template v-if="innerForm">
      <div v-for="(img,ind) in innerForm.images" :key="img" class="flex">
        <input :value="img" class="w-full border border-zinc-400 rounded-l-lg px-1" @input="changeImages($event,ind)"/>
        <i class='bx bxs-trash-alt px-2 py-1 bg-rose-500 text-rose-200 cursor-pointer rounded-r-lg'
           @click="removeImage(ind)"></i>
      </div>
    </template>
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
import {defineProps, defineEmits, ref, onMounted, computed} from "vue";
import {SliderProps} from "@/core/interfaces/props/slider";
import {useEditForm} from "@/core/composables";

const props = defineProps<{ form: SliderProps }>()
const emits = defineEmits(['save'])

const {
  innerForm,
  isChanged,
  save,
  close
} = useEditForm<SliderProps>(props, emits)

const changeImages = (v: any, ind: number) => {
  if (!innerForm.value?.images)
    return
  innerForm.value.images[ind] = v.target.value
}
const removeImage = (ind: number) => {
  if (!innerForm.value?.images)
    return
  innerForm.value.images.splice(ind, 1)
}
</script>

<style scoped>

</style>