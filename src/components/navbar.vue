<template>
   <div class="navbar">
      <div class="toggle-lang">
         <span
            :style="
               this.getLang
                  ? { color: 'var(--white)' }
                  : {  }
            "
         >EN</span>
         <input type="checkbox" id="switch" />
         <label for="switch" @click="switchLang"></label>
         <span
            :style="
               !this.getLang
                  ? { color: 'var(--white)' }
                  : {  }
            "
         >FR</span>
      </div>
      <div class="anchor">
         <a href="#home"
            ref="home"
            @click="setActive('home')"
         >{{
               this.getLang
                  ? navbar.home.en
                  : navbar.home.fr
            }}
         </a>
         <a href="#about"
            ref="about"
            @click="setActive('about')"
         >{{
               this.getLang
                     ? navbar.about.en
                     : navbar.about.fr
            }}
         </a>
         <a href="#work"
            ref="work"
            @click="setActive('work')"
         >{{
               this.getLang
                     ? navbar.work.en
                     : navbar.work.fr
            }}
         </a>
         <a href="#contact"
            ref="contact"
            @click="setActive('contact')"
         >{{
               this.getLang
                     ? navbar.contact.en
                     : navbar.contact.fr
            }}
         </a>
      </div>
   </div>
</template>

<script>
import { mapGetters, mapActions } from "vuex";
import navbar from "../assets/text.js";

export default {
   name: "navbar",
   methods: {
      switchLang() {
         this.switchLang();
      },

      setActive(anchor) {
         document.querySelectorAll(".anchor > a")
               .forEach(e => {
                  e.removeAttribute('class');
               });
         this.$refs[anchor].classList.add("anchor_active");
      },

      ...mapActions(['switchLang']),
   },
   computed: {
      ...mapGetters(['getLang']),
   },
   data() {
      return {
         navbar
      }
   }
}
</script>

<style scoped>
.navbar {
   width: 100%;
   height: 110px;

   position: fixed;
   top: 0;
   left: 0;

   display: flex;
   align-self: center;
   justify-content: space-between;
}

.toggle-lang {
   width: 200px;
   height: 100%;

   display: flex;
   align-items: center;
   justify-content: center;
}

input[type=checkbox]{
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
   content: '';
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

.anchor {
   width: 440px;
   display: flex;
   align-items: center;
   justify-content: space-between;
   padding-inline: 5px;
   margin-right: 75px;
   position: relative;
}

.anchor a {
   text-decoration: none;
   width: 66px;
   color: var(--dark-grey);
   font-size: 15px;
   font-family: Lato-Bold, sans-serif;
   font-weight: bolder;
   display: flex;
   align-self: center;
   justify-content: center;
}

.anchor a.anchor_active {
   color: var(--white);
}

/*
Allows you to add a small light above the anchor you're hovering
It's not the best choice, since it conflicts with the animation,
and moreover, when you finished hovering, it basically remove
the hover, which isn't really nice.

.anchor a:not(.anchor_active):hover:before {
   width: 110px;
   height: 110px;
   background-color: var(--white);
   border-radius: 50%;
   animation: anchor-shadow 0.3s ease-in;
   --topix: -38px;
   box-shadow: 0 24px 65px var(--topix) rgba(255, 255, 255, 0.3);
   transform: translateY(-100%);
   content: "";
   position: absolute;
   align-self: center;
}
 */

.anchor a:hover {
   color: var(--white);
}

a.anchor_active:before {
   width: 110px;
   height: 110px;
   background-color: var(--white);
   border-radius: 50%;
   animation: anchor-shadow 0.6s ease-in-out;
   --topix: -10px;
   box-shadow: 0 24px 65px var(--topix) rgba(255, 255, 255, 0.3);
   transform: translateY(-100%);
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