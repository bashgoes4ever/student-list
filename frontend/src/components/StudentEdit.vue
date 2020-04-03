<template>
    <v-container fluid>
        <v-row
                align="center"
                justify="center"
        >
            <v-col cols="10">

                <v-form
                        ref="form"
                >
                    <v-text-field
                            v-model="name"
                            :counter="128"
                            label="ФИО"
                            required
                    ></v-text-field>

                    <v-menu
                            ref="menu"
                            v-model="menu"
                            :close-on-content-click="false"
                            :nudge-right="40"
                            lazy
                            transition="scale-transition"
                            offset-y
                            full-width
                            min-width="290px"
                    >
                        <template v-slot:activator="{ on }">
                            <v-text-field
                                    v-model="date"
                                    label="Дата рождения"
                                    readonly
                                    v-on="on"
                            ></v-text-field>
                        </template>
                        <v-date-picker
                                ref="picker"
                                v-model="date"
                                :max="new Date().toISOString().substr(0, 10)"
                                min="1950-01-01"
                                @change="save"
                        ></v-date-picker>
                    </v-menu>

                    <v-select
                            v-model="mark"
                            :items="marks"
                            item-text="value"
                            label="Успеваемость"
                            required
                    ></v-select>

                    <v-btn @click.prevent="editStudent" :disabled="!date || !name || !mark">Изменить информацию</v-btn>
                </v-form>

            </v-col>
        </v-row>
    </v-container>
</template>

<script>
    export default {
        name: "StudentEdit",
        data: () => ({
            date: null,
            menu: false,
            marks: null,
            name: '',
            mark: ''
        }),
        created: function() {
            this.getMarks()
            this.getStudent(this.$route.params.id)
        },
        watch: {
            menu(val) {
                val && setTimeout(() => (this.$refs.picker.activePicker = 'YEAR'))
            }
        },
        methods: {
            save(date) {
                this.$refs.menu.save(date)
            },
            getMarks() {
                this.axios.get('http://127.0.0.1:8000/api/v1/marks/').then(r => (
                    this.marks = r.data
                ))
            },
            getStudent(id) {
                this.axios.get('http://127.0.0.1:8000/api/v1/students/?id='+id).then(r => {
                    this.mark = r.data.mark.value
                    this.name = r.data.name
                    this.date = r.data.date_birth
                })
            },
            editStudent() {
                this.axios.patch('http://127.0.0.1:8000/api/v1/students/', {
                    name: this.name,
                    date: this.date,
                    mark: this.mark,
                    id: this.$route.params.id
                }).then(() => {
                    this.$router.push('/')
                })
            }
        }
    }
</script>

<style scoped>

</style>