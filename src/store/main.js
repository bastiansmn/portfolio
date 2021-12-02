import {createStore} from "vuex";

export default createStore({
    state: {
        eng: false,
        enableObserver: true,
		modileVersion: false
    },
    mutations: {
        SWITCH_LANG(state) {
            state.eng = !state.eng;
        },
        SET_LANG(state, english) {
            state.eng = english;
        },
        SET_OBSERVER(state, enableObserver) {
            state.enableObserver = enableObserver;
        },
		SET_VERSION(state, version) {
		 	state.modileVersion = (version === "mobile");
		}
    },
    actions: {
        switchLang(context) {
            context.commit('SWITCH_LANG');
        },
        setLang(context, english=false) {
            context.commit('SET_LANG', english);
        },
        setObserver(context, enable) {
            context.commit('SET_OBSERVER', enable);
        },
		setMobile(context) {
			context.commit('SET_VERSION', "mobile");
		},
		setDesktop(context) {
			context.commit("SET_VERSION", "other");
		}
    },
    getters: {
        getLang: state => {
            return state.eng;
        },
        observerEnabled: state => {
            return state.enableObserver;
        },
		isMobile: state => {
			return state.modileVersion;
		}
    }
})