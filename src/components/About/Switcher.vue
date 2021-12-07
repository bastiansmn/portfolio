<template>
	<div class="Switcher">
		<div
			class="buttons">
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
		</div>
		<span
		 	class="underline"
		 	ref="underline"></span>
		<div class="continue">
			<ContinueButton
				:link="'#work'"	
			>
				<div>
					{{
						this.getLang
							? text.soft_skills.continue_button.first.en
							: text.soft_skills.continue_button.first.fr
					}}
				</div>
				<div>
					{{
						this.getLang
								? text.soft_skills.continue_button.second.en
								: text.soft_skills.continue_button.second.fr
					}}
				</div>
			</ContinueButton>	
		</div>
	</div>
</template>

<script>
import { mapGetters } from 'vuex';
import text from "../../assets/text.js";
import ContinueButton from "../utils/ContinueButton.vue";

export default {
	name: "Switcher",
	components: {
		ContinueButton
	},
	computed: {
		...mapGetters(["getLang"]),
	},
	methods: {
		changeContent() {
			this.$emit("change");
			this.$refs["underline"].style.transform = 
				this.showSoftSkills
					? "translateX(55px)"
					: "translateX(-55px)";
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
@media screen and (max-width: 931px) {
	.Switcher {
		width: 60%;
		align-self: center;
		position: absolute;
    	bottom: 0;
    	left: 50%;
    	transform: translateX(-50%);
	}

	.underline {
		margin-bottom: 10%;
	}
}

@media screen and (min-width: 930px) {
	.Switcher {
		left: 0;
		width: 45%;
		position: absolute;
		bottom: 0;
	}

	.underline {
		margin-bottom: 3vh;
	}
}

.Switcher {
	display: flex;
	flex-direction: column;
	align-items: center;
	justify-content: space-between;
}


.buttons {
	height: 27px;
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
	color: var(--dark-grey);
}

.clicker.button_active {
	color: var(--white);
	left: var(--translation);
}

.underline {
	width: 70px;
	height: 2px;
	transform: translateX(-55px);
	transform-origin: center;
	background: var(--white);
	transition: all .8s ease-in-out;
}
</style>