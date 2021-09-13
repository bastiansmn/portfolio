<template>
   <div class="vertical-scroll-animation">
      <div class="scroller">
         <slot/>
      </div>
   </div>
</template>

<script>
export default {
   name: "VerticalScrollAnimation",
}
</script>

<style scoped>
.vertical-scroll-animation {
   min-height: 29px;
   max-height: 29px;
   width: 120px;
   margin-left: 30px;
   overflow-y: hidden;
}

.scroller {
   display: flex;
   flex-direction: column;
   align-items: center;
   justify-content: flex-start;
   width: 100%;

   animation: text 8s infinite ease-in-out;
}

@keyframes text {
   0% {
      transform: translateY(0);
   }
   25% {
      transform: translateY(0);
   }
   50% {
      transform: translateY(-29px);
   }
   75% {
      transform: translateY(-29px);
   }
   100% {
      transform: translateY(0);
   }
}
</style>