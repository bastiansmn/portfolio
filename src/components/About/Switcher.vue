<template>
	<div class="Switcher">
		<div>
			<div 
				class="clicker"
				:class="showSoftSkills && 'button_active'"
				@click="!showSoftSkills && changeContent()">
				{{
					this.getLang 
						? text.switcher.soft_skills.en
						: text.switcher.soft_skills.fr
				}}
			</div>
			<span> - </span>
			<div class="clicker"
				:class="!showSoftSkills && 'button_active'"
				@click="showSoftSkills && changeContent()">
				{{
					this.getLang 
						? text.switcher.languages.en
						: text.switcher.languages.fr
				}}
			</div>
			<span
			 class="underline"
			 ref="underline"></span>
		</div>
	</div>
</template>

<script>
import { mapGetters } from 'vuex';
import text from "../../assets/text.js";

export default {
	name: "Switcher",
	components: {
		
	},
	computed: {
		...mapGetters(["getLang"]),
	},
	methods: {
		changeContent() {
			this.$emit("change");
			this.$refs["underline"].style.left = 
				this.showSoftSkills
					? "110px"
					: "0";
			this.$refs["underline"].style.width = "50px";
			setTimeout(_ => {
				this.$refs["underline"].style.width = "70px";
			}, 400);
			this.showSoftSkills = !this.showSoftSkills;
		}
	},
	data() {
		return {
			showSoftSkills: true,
			text,
		}
	},
}
</script>

<style scoped>
.Switcher {
	position: absolute;
	bottom: 0;
	left: 0;
	width: 45%;
	display: flex;
	align-items: center;
	justify-content: center;
}

.Switcher > div {
	position: relative;
	height: 36px;
	min-width: 180px;
	max-width: 180px;
	display: flex;
	flex-direction: row;
	align-items: center;
	justify-content: space-between;
	color: var(--dark-grey);
	font-size: 17px;
	font-weight: 500;
}

.clicker {
	cursor: pointer;
}

.clicker.button_active {
	color: var(--white);
	left: var(--translation);
}

.underline {
	width: 70px;
	height: 2px;
	background: var(--white);

	position: absolute;
	bottom: 0;
	left: 0;

	transition: all .8s ease-in-out;
}
</style>