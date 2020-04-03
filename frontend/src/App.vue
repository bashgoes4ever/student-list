<template>
    <v-app id="sandbox">
        <v-navigation-drawer
                v-model="primaryDrawer.model"
                app
                overflow
        >
            <v-list dense class="menu">
                <router-link to="/" class="v-list-item v-list-item--link theme--dark">
                    <v-list-item-action>
                        <v-icon>mdi-home</v-icon>
                    </v-list-item-action>
                    <v-list-item-content>
                        <v-list-item-title>Главная</v-list-item-title>
                    </v-list-item-content>
                </router-link>
                <router-link to="/students/add" class="v-list-item v-list-item--link theme--dark">
                    <v-list-item-action>
                        <v-icon>mdi-account-plus</v-icon>
                    </v-list-item-action>
                    <v-list-item-content>
                        <v-list-item-title>Добавить студента</v-list-item-title>
                    </v-list-item-content>
                </router-link>
            </v-list>
        </v-navigation-drawer>

        <v-app-bar app>
            <v-app-bar-nav-icon @click.stop="primaryDrawer.model = !primaryDrawer.model"/>
        </v-app-bar>

        <v-content>
            <router-view></router-view>
        </v-content>

        <v-footer app>
            <span class="px-4">&copy; {{ new Date().getFullYear() }}</span>
        </v-footer>
    </v-app>
</template>

<script>
    export default {
        data: () => ({
            primaryDrawer: {
                model: null,
            }
        }),
    }
</script>

<style>
    a {
        text-decoration: none;
        color: inherit;
    }
    .menu {
        background-color: transparent;
    }
</style>