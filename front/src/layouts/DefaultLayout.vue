<template>
  <div class="min-h-full w-full flex flex-col space-y-2">
    <div class="h-20 w-full bg-blue-200">
      <label>
        <input type="checkbox">Редактировать
      </label>
    </div>
    <div class="flex items-stretch space-x-2">
      <div class="bg-white w-full">
        <slot></slot>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">


</script>
<script lang="ts">
export default {
  name: "DefaultLayout"
}
</script>

<style scoped lang="postcss">
.default-layout {
  @apply bg-blue-100 p-2;
}
</style>