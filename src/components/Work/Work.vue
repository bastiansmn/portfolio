<template>
	<div class="Work">
		<!-- Bubbles -->
		<div class="bubble white-gradient __medium" style="
			left: -11vw;
			bottom: 0;
			--xmove: -10px !important;
			--ymove: -5px !important;
		"></div>
		<div class="bubble blue-gradient __small" style="
			left: 2vw;
			bottom: 14vh;
			--xmove: 7px !important;
			--ymove: 2px !important;
		"></div>
		<div class="bubble blue-gradient __medium" style="
			right: -13vw;
			bottom: 11vh;
			--xmove: -10px !important;
			--ymove: -5px !important;
		"></div>
		<div class="bubble blue-gradient __small" style="
			right: 0;
			bottom: 27vh;
			--xmove: -10px !important;
			--ymove: -5px !important;
		"></div>
		<div class="bubble blue-gradient __small" style="
			left: 1vw;
			top: 5vh;
			--xmove: -10px !important;
			--ymove: -5px !important;
		"></div>

		<!-- TODO : Factor le carroussel dans un component -->
		<div class="carroussel">
			<h1>
				{{
					this.getLang
						? text.projects.title.en
						: text.projects.title.fr
				}}
			</h1>

			<button 
				@click="previousSlide()"
				:disabled="this.currentSlide === 0" 
				style="left: -10px;">
				<svg xmlns="http://www.w3.org/2000/svg" x="0px" y="0px"
				width="24" height="24"
				viewBox="0 0 172 172"
				style=" fill:#000000;"><g fill="none" fill-rule="nonzero" stroke="none" stroke-width="1" stroke-linecap="butt" stroke-linejoin="miter" stroke-miterlimit="10" stroke-dasharray="" stroke-dashoffset="0" font-family="none" font-weight="none" font-size="none" text-anchor="none" style="mix-blend-mode: normal"><path d="M0,172v-172h172v172z" fill="none"></path><g fill="#ffffff"><path d="M99.5665,150.5v0c9.5245,0 15.20767,-10.61383 9.92583,-18.54017l-30.6375,-45.95983l30.6375,-45.95983c5.28183,-7.92633 -0.40133,-18.54017 -9.92583,-18.54017v0c-3.98467,0 -7.71133,1.99233 -9.92583,5.3105l-34.15633,51.24167c-3.21067,4.816 -3.21067,11.08683 0,15.90283l34.15633,51.24167c2.2145,3.311 5.94117,5.30333 9.92583,5.30333z"></path></g></g></svg>
			</button>
			<button 
				@click="nextSlide()"
				:disabled="this.currentSlide === this.work.length - 1" 
				style="right: -10px;">
				<svg xmlns="http://www.w3.org/2000/svg" x="0px" y="0px"
				width="24" height="24"
				viewBox="0 0 172 172"
				style="fill: #000000;">
				<g fill="none" fill-rule="nonzero" stroke="none" stroke-width="1" stroke-linecap="butt" stroke-linejoin="miter" stroke-miterlimit="10" stroke-dasharray="" stroke-dashoffset="0" font-family="none" font-weight="none" font-size="none" text-anchor="none" style="mix-blend-mode: normal"><path d="M0,172v-172h172v172z" fill="none"></path><g fill="#ffffff"><path d="M79.6145,21.5v0c-9.5245,0 -15.2005,10.61383 -9.91867,18.54017l30.6375,45.95983l-30.6375,45.95983c-5.28183,7.92633 0.39417,18.54017 9.91867,18.54017v0c3.98467,0 7.71133,-1.99233 9.92583,-5.3105l34.15633,-51.24167c3.21067,-4.816 3.21067,-11.08683 0,-15.90283l-34.15633,-51.24167c-2.2145,-3.311 -5.934,-5.30333 -9.92583,-5.30333z"></path></g></g></svg>
			</button>

			<div class="slider" ref="slider">
				

				<div class="projects" ref="projects">
					<a 
						:href="proj.project_link"
						target="_blank"
						rel="noopener noreferrer"
						:key="proj.class"
						v-for="proj in work"
						class="project"
						ref="project"
						:class="proj.class"
					>
						<div class="blur__effect">
							<div class="text-content">
								<h1 style="margin-top: 0">{{ proj.name }}</h1>
								<p>
									{{
										this.getLang 
											? proj.description.en
											: proj.description.fr	
									}}
								</p>
								<h3>
									{{  
										this.getLang
											? text.projects.contenth3.en
											: text.projects.contenth3.fr
									}}
								</h3>
								<div class="techs-used">
									<div 
										class="tech"
										:key="tech"
										v-for="tech in proj.techs"
									>
										<img :src="`logos/${tech}.png`" alt="">
									</div>
								</div>
							</div>
						</div>
						<div class="image">
							<img :src='`work/${proj.class}.png`' alt="">
						</div>
					</a>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
import { mapGetters } from 'vuex';
import text from "../../assets/text.js";
import work from "../../assets/work.js";

export default {
	name: "Work",
	components: {
		
	},
	computed: {
		...mapGetters(["getLang", "isMobile"]),
	},
	methods: {
		updateScroll() {
			this.$refs["slider"].scrollTo({
				left: (this.$refs["projects"].scrollWidth / this.work.length)*(this.currentSlide % this.work.length),
				top: 0,
				behavior: "smooth"
			});
		},
		removeAutoscroll() {
			clearInterval(this.interval);
		},
		previousSlide() {
			this.removeAutoscroll();
			this.currentSlide = (this.currentSlide - 1) % this.work.length;
			this.updateScroll();
		},
		nextSlide() {
			this.removeAutoscroll();
			this.currentSlide = (this.currentSlide + 1) % this.work.length;
			this.updateScroll();
		},
	},
	mounted() {
		if (!this.isMobile) {
			// TODO : Connecter le scroll du carroussel avec currentSlide
			const slider = this.$refs["slider"];
			slider.addEventListener("mousewheel", _ => {
				clearInterval(this.interval);
				this.currentSlide = Math.round(slider.scrollLeft / slider.scrollWidth * this.work.length);
			});
			this.interval = setInterval(_ => {
				this.currentSlide = (this.currentSlide + 1) % this.work.length;
				this.updateScroll();
			}, 10_000);
		}
	},
	data() {
		return {
			currentSlide: 0,
			slideEnabled: true,

			interval: undefined,

			text,
			work
		}
	},
}
</script>

<style scoped lang="scss">
@media screen and (max-width: 930px) {
	.Work {
		margin-top: 50px;
	}

	.carroussel > button {
		display: none;
	}

	.slider {
		background: rgba(255, 255, 255, .1);
		backdrop-filter: blur(4px);

		position: relative;
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;

		width: 100%;

		border-radius: 12px;
		margin-top: 40px;

		& > .projects {
			--margin: 15px;
			margin: var(--margin);
			width: calc(100% - 2*var(--margin));
			height: calc(100% - 2*var(--margin));
			
			display: flex;
			flex-direction: column;

			& > .project {
				max-width: 100%;
				aspect-ratio: 16/9;
				
				&:not(:last-child) {
					margin-bottom: var(--margin);
				}

				& > .blur__effect {
					display: none;
				}

				& > .image {
					height: 100%;

					& > img {
						border-radius: 6px;
                  aspect-ratio: 16/9;
					   object-fit: cover;
                  height: 100%;
					}
				}
			}
		}
	}
}

@media screen and (min-width: 931px) {
	.carroussel {
		height: 70vh;
		position: relative;

		& > button {
			outline: none;
			background: var(--glass);
			border: none;
			position: absolute;
			top: 50%;
			height: 60px;
			width: 40px;
			color: black;
			z-index: 300;
			display: flex;
			align-items: center;
			justify-content: center;
			padding: 0;
			font-size: 25px;
			cursor: not-allowed;
			border-radius: 10%;

			&[disabled] g {
				fill: var(--glass) !important;
			}

			&:not([disabled]) {
				background: var(--dark-grey);
				color: var(--white);
				cursor: pointer;
			
				&:hover {
					transform: scale(1.1);
					background: var(--primary);
				}
			}
		}
	}
	
	.slider {
		position: relative;

		box-shadow: 20px 20px 50px rgba(0, 0, 0, .5);

		width: 100%;
		height: calc(100% - 73px);

		display: flex;
		align-items: center;
		justify-content: flex-start;
		overflow-x: scroll;

		& > .projects {
			height: 100%;

			display: flex;
			flex-direction: row;
			align-items: center;
			justify-content: flex-start;

			& > .project {
				height: 100%;
				max-height: 100%;
				aspect-ratio: 16/9;
				color: var(--white);
				position: relative;

				& > .blur__effect {
					position: absolute;
					height: 100%;
					width: 100%;
					opacity: 0;
					background: hsl(0, 0%, 0%, .5);
					backdrop-filter: blur(2px);
					visibility: hidden;
					z-index: 100;

					& > .text-content {
						position: absolute;
						right: 20px;
						bottom: 20px;

						width: 500px;
						padding: 40px;

						background: rgba(12, 12, 19, 0.9);

						backdrop-filter: blur(10px);

						border-radius: 10px;
						

						& > h3 {
							display: flex;
							flex-direction: row;
							align-items: center;
							justify-content: flex-end;
							text-decoration: underline;
						}

						& > .techs-used {
							width: 100%;
							display: flex;
							flex-direction: row-reverse;
							align-items: center;
							justify-content: flex-start;
							height: 50px;
							
							& > .tech {
								height: 100%;
								margin-inline: 5px;
								aspect-ratio: 1;

								& > img {
									height: 100%;
									aspect-ratio: 1;
									margin-inline: 10px;
								}
							}
						}
					}
				}

				&:hover {					
					& > .image {
						& > img {
							transform: scale(1.03);
						}
					}

					& > .blur__effect {
						opacity: 1;
						visibility: visible;
					}
				}

				& > .image { 

					overflow: hidden;
					height: 100%;
					width: 100%;
				
					& > img {
						width: 100%;
						height: 100%;
						aspect-ratio: 16/9;
					}
				}
			}
		}
	}
}

.Work {
	position: relative;

	width: 90%;
	min-height: 80vh;

	display: flex;
	align-items: center;
	justify-content: center;
}

.carroussel {
	position: relative;

	width: 90%;
	z-index: 999;

	& > h1 {
		color: var(--primary);
		width: 90%;
	}
}

/* Use scoll-snap-align only in firefox */
@-moz-document url-prefix() {
	.projects {
		scroll-snap-type: x mandatory;

		& > .project {
			scroll-snap-align: start;
		}
	}
}

@keyframes anim-button {
	0% {
		transform: translateX(0);
	}
	50% {
		transform: translateX(var(--toX));
	}
	100% {
		transform: translateX(0);
	}
}
</style>