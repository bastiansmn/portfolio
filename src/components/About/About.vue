<template>
         
	<!-- Bubbles -->
	<div class="bubble blue-gradient __medium" style="
      left: -1vw;
      bottom: 12vh;
      --xmove: -10px !important;
      --ymove: -5px !important;
   "></div>
	<div class="bubble white-gradient __small" style="
      left: 10vw;
      bottom: 10vh;
      --xmove: 7px !important;
      --ymove: 2px !important;
   "></div>
	<div class="bubble white-gradient __big" style="
      right: -15vw;
      top: 10vh;
      --xmove: -10px !important;
      --ymove: -5px !important;
   "></div>
	<div class="bubble blue-gradient __small" style="
      right: 9vw;
      top: 40vh;
      --xmove: -10px !important;
      --ymove: -5px !important;
   "></div>
	


   <div class="about">
		<AboutSlot>
			<template v-slot:content>
				<SoftSkills v-if="showSoftSkills" />
				<Languages v-else />
			</template>
			<template v-slot:switcher>
				<Switcher 
					@change="showSoftSkills = !showSoftSkills" />
			</template>
		</AboutSlot>
   </div>
</template>

<script>
import text from "../../assets/text";
import { mapGetters } from "vuex";
import AboutSlot from "./AboutSlot.vue";
import Switcher from "./Switcher.vue";
import Languages from "./Languages.vue";
import SoftSkills from "./SoftSkills.vue";

export default {
   name: "About",
	components: {
		AboutSlot,
		Switcher,
		Languages,
		SoftSkills
	},
   computed: {
      ...mapGetters(['getLang'])
   },
   mounted() {
      
   },
	methods: {
		
	},
   data() {
      return {
         text,
			showSoftSkills: true,
      }
   }
}
</script>

<style scoped>
@media screen and (max-width: 930px) {
	.about {
		height: 96vh;
		top: 0;
		align-items: flex-start;
	}
}

@media screen and (min-width: 931px) {
	.about {
		align-items: center;
		min-height: 80vh;
	}
}

.about {
   position: relative;
   width: 90%;

   display: flex;
   justify-content: center;
}

</style>