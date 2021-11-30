<template>
	<div class="anchor">
      <a href="#home"
         @click="setActive('home'); setObserver(false);"
      >{{
            this.getLang
               ? text.home.en
               : text.home.fr
         }}
      </a>
      <a href="#about"
         @click="setActive('about'); setObserver(false);"
      >{{
            this.getLang
                  ? text.about.en
                  : text.about.fr
         }}
      </a>
      <a href="#work"
         @click="setActive('work'); setObserver(false);"
      >{{
            this.getLang
                  ? text.work.en
                  : text.work.fr
         }}
      </a>
      <a href="#contact"
         @click="setActive('contact'); setObserver(false);"
      >{{
            this.getLang
                  ? text.contact.en
                  : text.contact.fr
         }}
      </a>
   </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex';
import setActive from "../../utils/function.js";
import text from "../../assets/text.js";

export default {
	name: "Links",
	components: {
		
	},
	methods: {
		setActive,
		...mapActions(["setObserver"])
	},
	computed: {
		...mapGetters(["getLang"])
	},
	data() {
		return {
			text,
		}
	},
}
</script>

<style scoped>
.anchor {
   width: 440px;
   display: flex;
   align-items: center;
   justify-content: space-between;
   padding-inline: 5px;
   margin-inline: 75px;
   position: relative;
}

.anchor > a {
   text-decoration: none;
   width: 66px;
   color: var(--dark-grey);
   font-size: 15px;
   font-weight: bolder;
   display: flex;
   align-self: center;
   justify-content: center;
}

.anchor > a:hover {
   color: var(--white);
}

.anchor > a.anchor_active {
   color: var(--white);
   transform: scale(1.07);
}

a.anchor_active:before {
   width: 110px;
   height: 110px;
   background-color: var(--white);
   border-radius: 50%;
   animation: anchor-shadow 0.6s ease-in-out;
   --topix: -10px;
   box-shadow: 0 24px 65px var(--topix) rgba(255, 255, 255, 0.3);
   transform: translateY(-111px);
   content: "";
   position: absolute;
   align-self: center;
}

@keyframes anchor-shadow {
   from {
      box-shadow: 0 24px 65px -50px rgba(255, 255, 255, 0.3);
   }
   to {
      box-shadow: 0 24px 65px var(--topix) rgba(255, 255, 255, 0.3);
   }
}
</style>