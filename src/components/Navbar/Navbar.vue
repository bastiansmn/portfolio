<template>
	<nav 
		class="navbar" 
		:style="this.isMobile && 
				 (this.navbarActive 
				 	? { transform: 'translateX(0)' }
					: { transform: 'translateX(100%)' })">
		<div class="toggle-lang">
			<span :style="this.getLang && { color: 'var(--white)' }">EN</span>
			<input type="checkbox" :checked="!this.getLang" id="switch" />
			<label for="switch" @click.prevent="switchLang"></label>
			<span :style="!this.getLang && { color: 'var(--white)' }">FR</span>
		</div>

		<Links />
	</nav>

	<button
		v-if="_ => {
			window.innerWidth < 931
		}"
		@click="this.navbarActive = !this.navbarActive" 
		class="show_navbar" 
		:active="this.navbarActive">
		<div></div>
		<div></div>
		<div></div>
	</button>
</template>

<script>
import { mapGetters, mapActions } from "vuex";
import text from "../../assets/text.js";
import Links from "./Links.vue";

export default {
	name: "navbar",
	components: {
		Links,
	},
	methods: {
		switchLang() {
			this.switchLang();
		},

		...mapActions(["switchLang"]),
	},
	computed: {
		...mapGetters(["getLang", "isMobile"]),
	},
	data() {
		return {
			text,
			navbarActive: false,
		};
	},
};
</script>

<style scoped lang="scss">
@media screen and (max-width: 930px) {
	.navbar {
		width: 150px;
		height: 100%;

		right: 0;

		flex-direction: column-reverse;
		justify-content: space-between;

		transform: translateX(100%);

		background: rgba(25, 27, 41, 0.9);
		box-shadow: 0 3px 7px rgba(0, 0, 0, 0.25);
		backdrop-filter: blur(7px);

		& > .toggle-lang {
			width: 90%;
			height: 70px;
		}
	}

	.show_navbar {
		position: fixed;
		top: 20px;
		right: 20px;
		width: 25px;
		height: 19px;
		outline: none;
		border: none;
		background: none;
		padding: 0;
		z-index: 99999;

		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: space-between;

		& > div {
			width: 100%;
			min-height: 3px;
			border-radius: 1px;
			background: var(--white);
		}

		&[active="true"] {
			height: 6px;

			& > div:nth-child(1) {
				transform: rotateZ(45deg) translateY(4px);
				transform-origin: center;
			}
			& > div:nth-child(3) {
				transform: rotateZ(-45deg) translateY(-4px);
				transform-origin: center;
			}

			& > div:nth-child(2) {
				opacity: 0;
			}
		}
	}
}

@media screen and (min-width: 931px) {
	.navbar {
		width: 100%;
		height: 110px;

		flex-direction: row;
		justify-content: space-between;
		
		& > .toggle-lang {
			width: 200px;
			height: 100%;
		}
	}

	.show_navbar {
		display: none;	
	}
}

.navbar {
	position: fixed;
	top: 0;
	z-index: 9999;
	
	display: flex;
	align-items: center;

	& > .toggle-lang {
		display: flex;
		align-items: center;
		justify-content: center;
	}
}


input[type="checkbox"] {
  height: 0;
  width: 0;
  display: none;
}

label {
  cursor: pointer;
  text-indent: -9999px;
  width: 32px;
  height: 18px;
  background-color: var(--primary);
  display: block;
  border-radius: 9px;
  position: relative;

  margin-inline: 15px;
  transition: none;
}

label:after {
  content: "";
  position: absolute;
  top: 2px;
  left: 2px;
  width: 14px;
  height: 14px;
  background: var(--white);
  border-radius: 90px;
  transition: 0.3s;
}

input:checked + label {
  background: var(--white);
}

input:checked + label:after {
  left: calc(100% - 2px);
  transform: translateX(-100%);
  background-color: var(--primary);
}

label:active:after {
  width: 16px;
}

span {
  color: var(--dark-grey);
}

.navbar__background {
  background: rgba(25, 27, 41, 0.7);
  box-shadow: 0 3px 7px rgba(0, 0, 0, 0.25);
  backdrop-filter: blur(4px);
}
</style>
