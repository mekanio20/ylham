import Sequelize from 'sequelize'
import { db } from './env.js'

export const DB = new Sequelize(db.name, db.user, db.password, {
  host: db.host,
  port: db.port,
  dialect: "postgres",
  logging: false,
});