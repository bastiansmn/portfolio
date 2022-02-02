<template>
   <a
         class="continue"
         :href="link"
   >
      <div class="arrow">
         <div class="background"></div>
      </div>
      <VerticalScrollAnimation>
         <slot />
      </VerticalScrollAnimation>
   </a>
</template>

<script>
import text from "../../assets/text.js";
import VerticalScrollAnimation from "./VerticalScrollAnimation.vue";
import {mapGetters} from "vuex";

export default {
   name: "ContinueButton",
   components: {VerticalScrollAnimation},
   data() {
      return {
         text
      }
   },
	props: {
		link: {
			type: String,
			required: true
		}
	},
   computed: {
      ...mapGetters(['getLang'])
   },
}
</script>

<style scoped>
.continue {
   cursor: pointer;
   display: flex;
   align-items: center;
   justify-content: space-between;
   height: 29px;
	color: var(--white);
	text-decoration: none;
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

</style>