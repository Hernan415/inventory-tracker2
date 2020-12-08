'use strict';
const {
  Model
} = require('sequelize');
module.exports = (sequelize, DataTypes) => {
  class sheet extends Model {
    /**
     * Helper method for defining associations.
     * This method is not a part of Sequelize lifecycle.
     * The `models/index` file will call this method automatically.
     */
    static associate(models) {
      // define association here
    }
  };
  sheet.init({
    title: DataTypes.STRING,
    desc: DataTypes.INTEGER
  }, {
    sequelize,
    modelName: 'sheet',
  });
  return sheet;
};