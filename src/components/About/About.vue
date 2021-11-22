<template>
   <div class="about">
      <div class="bubble blue-gradient __big" style="
         right: -150px;
         top: 146px;
      "></div>

		<!-- TODO : Transformer les composants dans des slots -->
         
		<AboutSlot>
			<template v-slot:content>
				<!-- "SoftSkills" si true, "Languages" sinon -->
				<SoftSkills v-if="showSoftSkills" />
				<Languages v-else />
			</template>
			<template v-slot:switcher>
				<!-- Switcher avec le comportement attendu -->
				<Switcher 
					@change="showSoftSkills = !showSoftSkills" />
			</template>
		</AboutSlot>
	   
   </div>
</template>

<script>
import programming_languages from "../../assets/programming_languages";
import text from "../../assets/text";
import { mapGetters } from "vuex";
import vanillaTilt from "vanilla-tilt";
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
      vanillaTilt.init(document.querySelectorAll(".tilting"), {
         max: 2,
         speed: 1000,
         perspective: 700,
         reverse: true,
         reset: true,
      });
   },
	methods: {
		
	},
   data() {
      return {
         programming_languages,
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