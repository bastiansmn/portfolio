<template>
	<div class="anchor">
      <a href="#home"
			:class="this.isMobile && 'mobile'"
         
      >{{
            this.getLang
               ? text.home.en
               : text.home.fr
         }}
      </a>
      <a href="#about"
			:class="this.isMobile && 'mobile'"
         
      >{{
            this.getLang
                  ? text.about.en
                  : text.about.fr
         }}
      </a>
      <a href="#work"
			:class="this.isMobile && 'mobile'"
         
      >{{
            this.getLang
                  ? text.work.en
                  : text.work.fr
         }}
      </a>
      <a href="#contact"
			:class="this.isMobile && 'mobile'"
         
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
import text from "../../assets/text.js";

export default {
	name: "Links",
	components: {
		
	},
	methods: {
		...mapActions(["setObserver"])
	},
	computed: {
		...mapGetters(["getLang", "isMobile"])
	},
	data() {
		return {
			text,
		}
	},
}
</script>

<style scoped lang="scss">
@media screen and (max-width: 930px) {
	.anchor {
		width: 100%;
		flex-direction: column;
		margin-block-start: 100px;

		& > a {
			margin-bottom: 70px;

			&.anchor_active:before {
				display: none;
			}
		}
	}
} 

@media screen and (min-width: 931px) {
	.anchor {
		width: 440px;
		flex-direction: row;
		padding-inline: 5px;
		margin-inline: 75px;
	}
}

.anchor {
   display: flex;
   align-items: center;
   justify-content: space-between;
   position: relative;

	& > a {
		text-decoration: none;
		color: var(--dark-grey);
		font-size: 15px;
		font-weight: bolder;
		display: flex;
		align-self: center;
		justify-content: center;
	}
}

.anchor > a:not(.mobile):hover {
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