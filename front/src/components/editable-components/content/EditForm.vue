<template>
  <div v-if="innerForm" class="bg-white space-y-3 overflow-auto">
    <rich-text v-model:value="innerForm.content" class="overflow-auto"></rich-text>
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
import {defineProps, defineEmits, ref} from "vue";
import {ContentProps} from "@/core/interfaces/props/content";
import {useEditForm} from "@/core/composables";
import RichText from "@/components/RichText.vue";

const test = ref('')
const props = defineProps<{ form: ContentProps }>()
const emits = defineEmits(['save'])
const {
  innerForm,
  isChanged,
  save,
  close
} = useEditForm<ContentProps>(props, emits)
</script>

<style scoped>

</style>