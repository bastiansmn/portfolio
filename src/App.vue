<template>
   <navbar />
   <div class="portfolio__content" ref="scrollable_content">
      <div id="home" class="section">
      	<Home class="home" />
		</div>
      <div id="about" class="section">
         <About />
      </div>
      <div id="work" class="section">
			<Work />
		</div>
      <div id="contact" class="section">
			<Contact />
		</div>
   </div>
</template>

<script>
import vanillaTilt from "vanilla-tilt";
import Navbar from "./components/Navbar/Navbar.vue";
import Home from "./components/Home/Home.vue";
import {mapActions, mapGetters} from "vuex";
import About from "./components/About/About.vue";
import Work from "./components/Work/Work.vue";
import Contact from "./components/Contact/Contact.vue";

export default {
   components: {
      About,
      Navbar,
      Home,
		Work,
		Contact
   },
   beforeMount() {
      !"fr-FR".includes(navigator.language) && this.setLang(true);
   },
   mounted() {
		// TODO : Vérifier la compatibilité avec mobile
      const anchors = document.querySelectorAll('.section');
      const observer = new IntersectionObserver((entries) => {
         entries.forEach(entry => {
            if (entry.isIntersecting) {
					document.querySelector(`a[href='#${entry.target.id}']`).classList.add("anchor_active");
					entry.target.classList.add("section_active");
					if (!this.isMobile) {
						if (entry.target.id === "home")
							document.querySelector(".navbar").classList.remove("navbar__background");
						else
							document.querySelector(".navbar").classList.add("navbar__background");
					}
            } else {
					document.querySelector(`a[href='#${entry.target.id}']`).classList.remove("anchor_active");
				}
         });
      }, {
         threshold: .55
      });
      anchors.forEach(anchor => {
         observer.observe(anchor)
      });
		
		window.onresize = _ => {
			if (!this.isMobile && window.innerWidth < 931)
				this.setMobile();
			else if (this.isMobile && window.innerWidth > 930)
				this.setDesktop();
		};

		vanillaTilt.init(document.querySelectorAll(".tilting"), {
         max: 7,
         speed: 1000,
         perspective: 700,
         reverse: true,
         reset: false,
         startX: 7,
         startY: -5,
      });
		vanillaTilt.init(document.querySelectorAll(".tilting-low"), {
         max: 3,
         speed: 1000,
         perspective: 700,
         reverse: true,
         reset: false,
         startX: -4,
         startY: 0,
      });

		if (window.innerWidth < 931)
			this.setMobile();
		else if (window.innerWidth > 930)
			this.setDesktop();
	
   },
   computed: {
      ...mapGetters(['observerEnabled', 'isMobile'])
   },
   methods: {
      ...mapActions(['setLang', 'setObserver', 'setMobile', 'setDesktop']),
   },
}
</script>

<style scoped>

@media screen and (min-width: 931px) {
	.section {
		padding-top: 110px;
	}

	#about, #work, #contact {
		min-height: 700px;
	}

	#contact {
		margin-top: 110px;
		height: calc(100vh - 110px);
	}
}

@media screen and (max-width: 930px) {
	#home {
		margin-top: 0 !important;
	}	

	#work {
		align-items: flex-start;
		height: unset;
	}

	.section {
		height: 100vh;
		width: 100vw;
	}
}

.portfolio__content {
   width: 100vw;
   height: 100vh;
   
   overflow-y: auto;
   overflow-x: hidden;
}

/* Use scoll-snap-align only in firefox */
@-moz-document url-prefix() {
	.portfolio__content {
		scroll-snap-type: y mandatory;

		width: 100vw;
		height: 100vh;
		
		overflow-y: auto;
		overflow-x: hidden;
	}

	
	.section {
		scroll-snap-align: start;
	}
}

.section {
	display: flex;
	align-items: center;
	justify-content: center;

	position: relative;
}
</style>
