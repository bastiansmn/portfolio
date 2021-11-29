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

<style>
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

.scroller > div {
   height: 29px;
   width: 120px;

   display: flex;
   align-items: center;
   justify-content: flex-start;
}

.scroller > div:nth-child(1) {
   animation: first-text-opacity 8s infinite ease-in-out;
}

.scroller > div:nth-child(2) {
   animation: second-text-opacity 8s infinite ease-in-out;
}


@keyframes first-text-opacity {
   0% {
      opacity: 1;
   }
   25% {
      opacity: 1;
   }
   50% {
      opacity: 0;
   }
   75% {
      opacity: 0;
   }
   100% {
      opacity: 1;
   }
}

@keyframes second-text-opacity {
   0% {
      opacity: 0;
   }
   25% {
      opacity: 0;
   }
   50% {
      opacity: 1;
   }
   75% {
      opacity: 1;
   }
   100% {
      opacity: 0;
   }
}
</style>