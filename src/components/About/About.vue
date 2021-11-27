<template>
         
	<!-- Bubbles -->
	<div class="bubble blue-gradient __medium" style="
      left: -10px;
      bottom: 100px;
      --xmove: -10px !important;
      --ymove: -5px !important;
   "></div>
	<div class="bubble white-gradient __small" style="
      left: 130px;
      bottom: 100px;
      --xmove: 7px !important;
      --ymove: 2px !important;
   "></div>
	<div class="bubble white-gradient __big" style="
      right: -150px;
      top: 110px;
      --xmove: -10px !important;
      --ymove: -5px !important;
   "></div>
	<div class="bubble blue-gradient __small" style="
      right: 100px;
      top: 410px;
      --xmove: -10px !important;
      --ymove: -5px !important;
   "></div>
	<div class="bubble white-gradient __small" style="
      left: 100px;
      top: 50px;
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
.about {
   position: relative;
   min-height: 80vh;
   width: 90%;

   display: flex;
   align-items: center;
   justify-content: center;
}

</style>