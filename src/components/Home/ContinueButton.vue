<template>
   <a
         class="continue"
         href="#about"
         @click="setActive('about')"
   >
      <div class="arrow">
         <div class="background"></div>
      </div>
      <VerticalTextAnimation>
         <div class="text-inside first">
            {{
               this.getLang
                  ? text.continue_button.first.en
                  : text.continue_button.first.fr
            }}
         </div>
         <div class="text-inside second">
            {{
               this.getLang
                     ? text.continue_button.second.en
                     : text.continue_button.second.fr
            }}
         </div>
      </VerticalTextAnimation>
   </a>
</template>

<script>
import text from "../../assets/text";
import VerticalTextAnimation from "./VerticalScrollAnimation.vue";
import setActive from "../../utils/function";
import {mapGetters} from "vuex";

export default {
   name: "ContinueButton",
   components: {VerticalTextAnimation},
   data() {
      return {
         text
      }
   },
   computed: {
      ...mapGetters(['getLang'])
   },
   methods: {
      setActive
   }
}
</script>

<style scoped>
.continue {
   position: absolute;
   bottom: 7%;
   padding: 1px;
   cursor: pointer;
   display: flex;
   align-items: center;
   justify-content: space-between;
   height: 29px;
}

.arrow {
   position: relative;
   width: 29px;
   height: 29px;
   background-color: var(--dark-grey);
   border-radius: 50%;
}

.background {
   display: flex;
   align-items: center;
   justify-content: center;

   width: 100%;
   height: 100%;
}

.background:before {
   content: "";
   position: relative;
   height: 4px;
   border-radius: 2px;
   width: 13px;
   background-color: var(--white);
   transition: background-color .2s ease-in-out;
   transform: rotate(45deg);
   transform-origin: bottom right;
   top: 5px;
}

.background:after {
   content: "";
   position: relative;
   height: 4px;
   border-radius: 2px;
   width: 13px;
   background-color: var(--white);
   transition: background-color .2s ease-in-out;
   transform: rotate(-45deg);
   transform-origin: bottom left;
   top: 5px;
}

.continue:hover .background:after, .continue:hover .background:before {
   background: var(--primary);
}

.continue:hover .arrow {
   background-color: var(--white);
}

.text-inside {
   height: 29px;
   width: 120px;

   display: flex;
   align-items: center;
   justify-content: flex-start;
}

a {
   color: var(--white);
   text-decoration: none;
}

.text-inside.first {
   animation: first-text-opacity 8s infinite ease-in-out;
}

.text-inside.second {
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