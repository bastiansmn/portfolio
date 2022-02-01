<template>
   <div class="home">
		<!-- TODO max/min sur les positions des bulles ? -->
      <div class="bubble blue-gradient __big" style="
         left: -12vw;
         top: 14vh;
      "></div>
      <div class="bubble white-gradient __medium" style="
         right: -5vw;
         bottom: 20vh;
      "></div>
      <div class="bubble white-gradient __small" style="
         right: 10vw;
         top: 8vh;
      "></div>
      <div class="bubble blue-gradient __small" style="
         right: 10vw;
         top: 37vh;
         --xmove: -10px !important;
         --ymove: -5px !important;
      "></div>

      <div class="introducing">
         <img
               class="avatar card tilting"
               src="/avatar.jpg"
               alt="Bastian Somon"
         />
         <div class="presentation__text reveal-rtl">
            <p>
               {{
                  this.getLang
                        ? text.introducing.header.en
                        : text.introducing.header.fr
               }}
            </p>
            <h1>
               {{
                  this.getLang
                        ? text.introducing.name.en
                        : text.introducing.name.fr
               }}
            </h1>
            <p>
               {{
                  this.getLang
                        ? text.introducing.p.en
                        : text.introducing.p.fr
               }}
            </p>
         </div>
      </div>

      <ContinueButton class="continue" :link="'#about'">
			<div>
            {{
               this.getLang
                  ? text.continue_button.first.en
                  : text.continue_button.first.fr
            }}
         </div>
         <div>
            {{
               this.getLang
                     ? text.continue_button.second.en
                     : text.continue_button.second.fr
            }}
         </div>
		</ContinueButton>
   </div>
</template>

<script>
import text from "../../assets/text.js";
import {mapGetters} from "vuex";
import ContinueButton from "../utils/ContinueButton.vue";

export default {
   name: "Home",
   components: {ContinueButton},
   mounted() {
		
   },
   computed: {
      ...mapGetters(['getLang'])
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
	.home {
		width: 85%;
		height: 80%;

		& > .introducing {
			margin-top: 0;
			width: 100%;
			height: calc(100% - 100px);
			flex-direction: column;

			& > .presentation__text {
				padding-block: 20px;
				width: 90%;

				& > p {
					font-size: min(2.5vh, 17px);
				}
				& > h1 {
					font-size: min(6vh, 40px);
				}
			}

			& > .avatar {
				height: 40%;
				max-height: 190px;
			}
		}

		& > .continue {
			bottom: 0;
		}
	}
}

@media screen and (min-width: 931px) {
	.home {
		width: 100%;
   	height: 80vh;

		& > .introducing {
			margin-top: min(15vh, 150px);
			width: 65%;
			max-width: 850px;
			min-width: 600px;
			height: 220px;
			padding: 10px;

			& > .avatar {
				height: 240px;
				aspect-ratio: 1;
			}

			& > .presentation__text {
				width: calc(100% - 330px);
				max-width: 450px;
				height: 90%;	
			}
		}

		& > .continue {
			bottom: 7%;
		}
	}
}

.home {
   position: relative;
   display: flex;
   justify-content: center;


	& > .introducing {
		display: flex;
		align-items: center;
		justify-content: space-between;

		z-index: 10;

		& > .card {
			position: relative;
			margin: 10px;
			overflow: hidden;
			border-radius: 15px;
			box-shadow: 20px 20px 50px rgba(0, 0, 0, .5);
			display: flex;
			align-items: center;
			justify-content: center;
			z-index: 100;
		}

		& > .avatar {
			aspect-ratio: 1;
			border-radius: 3vh;
		}

		& > .presentation__text {
			display: flex;
			flex-direction: column;
			align-items: flex-start;
			justify-content: center;
		}
	}

	& > .continue {
		position: absolute;
		z-index: 100;
	}
}
</style>