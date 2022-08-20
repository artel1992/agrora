<template>
  <div class="w-full" v-if="form">
    <div id="default-carousel" class="relative">
      <!-- Carousel wrapper -->
      <div class="overflow-hidden relative h-56 rounded-lg sm:h-64 xl:h-80 2xl:h-96">
        <div class="duration-700 ease-in-out" v-for="(image,ind) in form.images" :key="ind"
             :class="{'hidden':currentImageIndex !== ind}">
          <span
              class="absolute top-1/2 left-1/2 text-2xl font-semibold text-white -translate-x-1/2 -translate-y-1/2 sm:text-3xl text-gray-800">alt image</span>
          <img :src="image"
               class="block absolute top-1/2 left-1/2 w-full -translate-x-1/2 -translate-y-1/2" alt="...">
        </div>
      </div>
      <!-- Slider indicators -->
      <div class="flex absolute bottom-5 left-1/2 z-30 space-x-3 -translate-x-1/2">
        <button v-for="(image,ind) in component.structure.props.images" :key="ind"
                class="w-3 h-3 rounded-full bg-blue-500/30"
                :class="{'bg-blue-500':ind===currentImageIndex}" @click="currentImageIndex=ind"></button>
      </div>
      <!-- Slider controls -->
      <button type="button"
              @click="toPrevImage"
              class="flex absolute top-0 left-0 z-30 justify-center items-center px-4 h-full cursor-pointer group focus:outline-none"
      >
            <span
                class="inline-flex justify-center items-center
                w-8 h-8 rounded-full sm:w-10 sm:h-10 bg-white/30
                 bg-gray-800/30
                 group-hover:bg-gray-800/60
                 group-focus:ring-gray-800/70
                 group-hover:bg-blue-500/50
                 group-focus:ring-4
                 group-focus:ring-white
                 group-focus:outline-none">
                <svg class="w-5 h-5 sm:w-6 sm:h-6 text-blue-800" fill="none" stroke="currentColor"
                     viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round"
                                                                                  stroke-linejoin="round"
                                                                                  stroke-width="2"
                                                                                  d="M15 19l-7-7 7-7"></path></svg>
            </span>
      </button>
      <button type="button"
              class="flex absolute top-0 right-0 z-30 justify-center items-center px-4 h-full cursor-pointer group focus:outline-none"
              @click="toNextImage">
            <span
                class="inline-flex justify-center
                items-center w-8 h-8 rounded-full
                sm:w-10 sm:h-10 bg-white/30
                bg-gray-800/30
                group-hover:bg-blue-500/50
                group-focus:ring-4
                group-focus:ring-white
                group-focus:ring-gray-800/70
                group-focus:outline-none">
                <svg class="w-5 h-5 sm:w-6 sm:h-6 text-blue-800" fill="none" stroke="currentColor"
                     viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round"
                                                                                  stroke-linejoin="round"
                                                                                  stroke-width="2"
                                                                                  d="M9 5l7 7-7 7"></path></svg>
            </span>
      </button>
    </div>
  </div>
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
  name: "SliderComponent"
}
</script>
<script setup lang="ts">
import {defineProps, defineEmits, ref, watch, onMounted, Ref} from "vue";
import {SliderProps} from "@/core/interfaces/props/slider";
import {EditableComponent} from "@/core/interfaces";
import {useEditableComponent} from "@/core/composables";
import EditForm from "@/components/editable-components/slider/EditForm.vue";
import {$vfm} from "vue-final-modal";

const props = defineProps<{ component: EditableComponent<SliderProps> }>()
const emits = defineEmits<{
  (eventName: 'update:component', form: EditableComponent<SliderProps>): void
}>()

const {
  modalName,
  modalOpen,
  form,
  saveForm
} = useEditableComponent<SliderProps>('edit-slider', props, emits)
const currentImageIndex = ref(0)




const toPrevImage = () => {
  if (currentImageIndex.value === 0) {
    currentImageIndex.value = props.component.structure.props.images.length - 1
    return
  }
  currentImageIndex.value--
}
const toNextImage = () => {
  if (currentImageIndex.value === props.component.structure.props.images.length - 1) {
    currentImageIndex.value = 0
    return
  }
  currentImageIndex.value++
}
</script>

<style scoped lang="postcss">

</style>