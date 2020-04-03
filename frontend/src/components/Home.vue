<template>
    <v-container fluid>
        <v-row
                align="center"
                justify="center"
        >
            <v-col cols="10">
                <v-simple-table dark v-if="students != null && students.length > 0">
                    <template v-slot:default>
                        <thead>
                        <tr>
                            <th class="text-left">Имя</th>
                            <th class="text-left">Дата рождения</th>
                            <th class="text-left">Успеваемость</th>
                            <th></th>
                        </tr>
                        </thead>
                        <tbody>
                        <tr v-for="(item, i) in students" :key="i" class="student-row">
                            <td>{{ item.name }}</td>
                            <td>{{ formatDate(item.date_birth) }}</td>
                            <td>{{ item.mark.value }}</td>
                            <td class="buttons">
                                <router-link :to="`students/edit/${item.id}`" class="student__btn">
                                    <v-icon>mdi-lead-pencil</v-icon>
                                </router-link>
                                <v-icon class="delete-btn student__btn"
                                        @click="dialog = true; delete_item = {'item_id': item.id, 'index': i}"
                                >mdi-delete
                                </v-icon>
                            </td>
                        </tr>
                        </tbody>
                    </template>
                </v-simple-table>
                <v-alert type="info" v-else-if="students != null">
                    Нет данных ни об одном студенте
                </v-alert>
            </v-col>
        </v-row>
        <v-row justify="center">
            <v-dialog v-model="dialog" persistent max-width="290">
                <v-card>
                    <v-card-title class="headline">Удалить данные студента?</v-card-title>
                    <v-card-actions>
                        <v-spacer></v-spacer>
                        <v-btn color="green darken-1" text @click="deleteStudent()" :disabled="on_delete">Удалить</v-btn>
                        <v-btn color="green darken-1" text @click="dialog = false">Отмена</v-btn>
                    </v-card-actions>
                </v-card>
            </v-dialog>
        </v-row>
    </v-container>
</template>

<script>
    import moment from 'moment'

    export default {
        name: 'Home',
        data: () => ({
            students: null,
            dialog: false,
            delete_item: {},
            on_delete: false
        }),
        created: function () {
            this.getStudents()
        },
        methods: {
            getStudents() {
                this.axios.get('http://127.0.0.1:8000/api/v1/students/').then(r => (
                    this.students = r.data
                ))
            },
            formatDate(date) {
                return moment(date).format('DD.MM.YYYY')
            },
            deleteStudent() {
                this.on_delete = true
                this.axios.delete('http://127.0.0.1:8000/api/v1/students/', {data: {
                    id: this.delete_item.item_id
                }}).then(() => {
                    this.on_delete = false
                    this.dialog = false
                    this.students.splice(this.delete_item.index, 1)
                })
            }
        }
    }
</script>

<style scoped>
    .buttons {
        text-align: right;
    }

    .student__btn {
        transition: all .3s;
        opacity: 0;
    }

    .delete-btn {
        cursor: pointer;
        margin-left: 5px;
    }

    .student-row:hover .student__btn {
        opacity: 1;
    }

    .v-card__title {
        word-break: break-word;
    }
</style>