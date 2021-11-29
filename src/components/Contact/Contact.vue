<template>
	<div class="Contact">
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

		<div class="form">
			<h1>{{
					this.getLang
						? text.contact_comp.contact_me.en
						: text.contact_comp.contact_me.fr
				}}</h1>
			<form @submit.prevent="submitForm($event)">
				<div class="inputs">
					<textarea 
						required
						autocomplete="off"
						spellcheck="false"
						type="text" 
						id="message"
						v-model="form.message"
						:placeholder="
							this.getLang 
								? text.contact_comp.message.en 
								: text.contact_comp.message.fr">
					</textarea>
					<input
						required	
						autocomplete="off"
						type="text" 
						id="name" 
						v-model="form.name"
						:placeholder="
						this.getLang 
							? text.contact_comp.name.en 
							: text.contact_comp.name.fr">
				</div>
				<div class="sender">
					<p>
						{{
							this.getLang
								? text.contact_comp.description.en
								: text.contact_comp.description.fr
						}}
					</p>
					<button type="submit">
						{{
							this.getLang 
								? text.contact_comp.send.en
								: text.contact_comp.send.fr
						}}
					</button>
				</div>
			</form>
		</div>

		<div class="socials">
			<a
				target="_blank"
				class="social_media"
				v-for="social in socials"
				:href="social.link"
				:key="social.classname"
				:class="social.classname">
				<img :src="`socials/${social.classname}.png`" :alt="social.name">
			</a>
		</div>
	</div>
</template>

<script>
import { mapGetters } from 'vuex';
import text from "../../assets/text.js";
import socials from "../../assets/socials.js";
import fs from "fs";


export default {
	name: "Contact",
	components: {
		
	},
	computed: {
		...mapGetters(["getLang"])
	},
	methods: {
		submitForm() {
			let name = this.form.name;
			let message = this.form.message;

			// TODO : Mailsender
			const body = {
				"name": name,
				"message": message
			};
			const data = JSON.stringify(body);
			fs.writeFile('messages.json', data, (err) => {
				if (err) {
					throw err;
				}
				console.log("Message écrit.");
			});

		},
	},
	mounted() {

	},
	data() {
		return {
			text,
			socials,

			form: {
				name: "",
				message: "",
			}
		}
	},
}
</script>

<style scoped lang="scss">
.Contact {
	position: relative;
	--padding: 120px;
	width: calc(100% - 2*var(--padding));
	height: calc(100% - 2*var(--padding));
	padding: var(--padding);

	display: flex;
	align-items: center;
	flex-direction: column;
	justify-content: center;
	align-items: center;

	& > .form {
		width: 80%;
		max-width: 1000px;
		height: calc(100% - 100px);

		margin-bottom: 100px;
		background: var(--glass);
		border-radius: 10px;		
		box-shadow: 20px 20px 50px rgba(0, 0, 0, .5);

		padding: 50px;

		& > form {
			display: flex;
			flex-direction: row;
			align-items: center;
			justify-content: space-between;

			height: calc(100% - 74px);
			
			& > div {
				height: 100%;
	
				display: flex;
				flex-direction: column;
			}

			& > .inputs {
				width: 60%;
				max-width: 600px;
				align-items: flex-start;
				justify-content: center;

				& > * {
					background: var(--dark-grey);
					outline: none;
					border: none;
					color: var(--white);
					padding: 5px;
					padding-inline: 15px;
				}
				
				& > input {
					border-radius: 99px;
					width: 50%;
					height: 30px;
					margin-top: 30px;
					font-size: 17px;
					align-self: flex-end;
				}

				& > textarea {
					width: calc(100% - 20px);
					height: calc(70% - 50px);
					border-radius: 12px;
					padding: 10px;
					font-family: Lato-Regular, sans-serif;
					font-size: 16px;
					resize: none;
				}
			}

			& > .sender {
				height: 75% !important;
				width: 35%;
				align-items: center;
				justify-content: space-between;

				& > button {
					cursor: pointer;
					background: var(--primary);
					color: var(--white);
					outline: none;
					border: none;
					border-radius: 5px;
					padding-block: 7px;
					padding-inline: 10px;
					font-size: 17px;

					&:hover {
						background: var(--white);
						color: var(--primary);
					}
				}
			}

		}
	}

	& > .socials {
		height: 50px;
		display: flex;
		flex-direction: row;
		align-items: center;
		justify-content: center;

		& > .social_media {
			height: 100%;
			aspect-ratio: 1;

			margin-inline: 15px;

			& > img {
				height: 100%;
				aspect-ratio: 1;
			}
		}
	}
}
</style>