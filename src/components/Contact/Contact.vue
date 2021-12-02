<template>
	<div class="Contact">
		<!-- Bubbles -->
		<div class="bubble blue-gradient __medium" style="
			left: -1vw;
			bottom: 10vh;
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
			right: -12vw;
			top: 8vh;
			--xmove: -10px !important;
			--ymove: -5px !important;
		"></div>
		<div class="bubble blue-gradient __small" style="
			right: 8vw;
			top: 40vh;
			--xmove: -10px !important;
			--ymove: -5px !important;
		"></div>
		<div class="bubble white-gradient __small" style="
			left: 10vw;
			top: 5vh;
			--xmove: -10px !important;
			--ymove: -5px !important;
		"></div>

		<div class="form reveal-ltr">
			<h1>{{
					this.getLang
						? text.contact_comp.contact_me.en
						: text.contact_comp.contact_me.fr
				}}</h1>
			<form v-if="!this.mailSent" @submit.prevent="submitForm($event)" ref="form">
				<div class="inputs">
					<textarea 
						required
						autocomplete="off"
						spellcheck="false"
						type="text" 
						id="message"
						name="message"
						:placeholder="
							this.getLang 
								? text.contact_comp.message.en 
								: text.contact_comp.message.fr"/>
					<input
						required	
						autocomplete="off"
						type="text" 
						id="name" 
						name="name"
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
			<div v-else class="mailSent">
				<img src="/icons/check.png" alt="">
				<div class="text">
					<h1>
						{{ 
							this.getLang 
								? text.emailed.h1.en
								: text.emailed.h1.fr
						}}
					</h1>
					<p>
						{{
							this.getLang
								? text.emailed.p.en
								: text.emailed.p.fr
						}}
					</p>
				</div>
			</div>
		</div>

		<div class="socials reveal-rtl">
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
import emailjs from 'emailjs-com';


export default {
	name: "Contact",
	components: {
		
	},
	computed: {
		...mapGetters(["getLang"])
	},
	methods: {
		submitForm() {
			emailjs.sendForm(import.meta.env.VITE_SERVICE_ID, import.meta.env.VITE_TEMPLATE_ID, this.$refs["form"], import.meta.env.VITE_USER_ID)
				.then(_ => {
						this.mailSent = true;
				}, (error) => {
						console.log('FAILED...', error.text);
				});
		},
	},
	mounted() {
		
	},
	data() {
		return {
			text,
			socials,

			mailSent: false
		}
	},
}
</script>

<style scoped lang="scss">
@media screen and (max-width: 930px) {
	.Contact {
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: space-between;

		width: 100%;
		height: 80%;

		& > .form {
			--padding: 20px;
			padding: var(--padding);
			width: calc(81% - 2*var(--padding));
			min-height: 450px;
			height: calc(95% - 100px - 2*var(--padding));
			background: var(--glass);
			border-radius: 10px;		
			box-shadow: 20px 20px 50px rgba(0, 0, 0, .5);

			& > h1 {
				font-size: min(4vh, 20px);
			}

			& > form {
				--padding: 10px;
				padding: var(--padding);
				height: calc(100% - 48px - 2*var(--padding));
				display: flex;
				flex-direction: column;
				align-items: center;
				justify-content: space-between;

				& > .sender {
					display: flex;
					flex-direction: column;
					align-items: center;
					justify-content: space-between;
					height: 37%;

					& > p {
						font-size: min(2.5vh, 15px);
					}

					& > button[type="submit"] {
						cursor: pointer;
						background: var(--primary);
						color: var(--white);
						outline: none;
						border: none;
						border-radius: 5px;
						padding-block: 7px;
						padding-inline: 10px;
						font-size: 17px;
					}
				}

				& > .inputs {
					width: 100%;
					height: 55%;

					display: flex;
					flex-direction: column;
					align-items: flex-end;
					justify-content: space-between;

					& > textarea {
						font-size: min(2.4vh, 14px);
  						font-family: Lato-Regular, sans-serif;
						--padding: 7px;
						--padding-inline: 10px;
						padding: var(--padding);
						padding-inline: var(--padding-inline);
						width: calc(100% - 2*var(--padding-inline));
						height: 70%;
						border-radius: 10px;
						background: var(--dark-grey);
						outline: none;
						border: none;
						color: var(--white);
					}

					& > input {
						font-size: min(2.2vh, 13px);
						--padding: 7px;
						--padding-inline: 10px;
						padding: var(--padding);
						padding-inline: var(--padding-inline);
						width: calc(80% - 2*var(--padding-inline));
						border-radius: 5px;
						background: var(--dark-grey);
						outline: none;
						border: none;
						color: var(--white);
					}
				}
			}

			& > .mailSent {
				width: 100%;
				--padding: 10px;
				padding: var(--padding);
				height: calc(100% - 48px - 2*var(--padding));
				width: calc(100% - 2*var(--padding));
				display: flex;
				flex-direction: column;
				align-items: center;
				justify-content: space-around;

				& > img {
					width: 30%;
					max-width: 100px;
					aspect-ratio: 1;
				}
			}
		}

		& > .socials {
			height: 50px;
			margin-top: 50px;

			& > .social_media {
				height: 50px;
				aspect-ratio: 1;
				margin-inline: 10px;
				& > img {
					height: 100%;
					aspect-ratio: 1;
				}
			}
		}
	}
}

@media screen and (min-width: 931px) {
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

			margin-bottom: 7vh;
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

			& > .mailSent {
				width: 100%;

				display: flex;
				flex-direction: row;
				align-items: center;
				justify-content: space-around;

				height: calc(100% - 74px);

				& > img {
					height: 40%;
					max-height: 300px;
					aspect-ratio: 1;
				}

				& > .text {
					width: 40%;
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
}

.inputs > * {
	
	&::placeholder {
		color: var(--white);
	}
}
</style>