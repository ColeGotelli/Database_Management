package com.company;
import java.sql.*;
import java.sql.Connection;
import java.sql.DriverManager;

public class DBConfig {

    public static void print(ResultSet results) throws SQLException {
        ResultSetMetaData data = results.getMetaData();
        int numberOfColumns = data.getColumnCount();

        for (int i = 1; i <= numberOfColumns; ++i) {
            if (i > 1)
                System.out.print(" ");
            String columnName = data.getColumnName(i);
            System.out.print(columnName);
        }
        System.out.println();

        while (results.next()) {
            for (int i = 1; i <= numberOfColumns; i++) {
                if (i > 1)
                    System.out.print(" ");
                String columnValue = results.getString(i);
                System.out.print(columnValue);
            }
            System.out.println();
        }
    }

    public static Connection getMySqlConnection(String IP, String DB, String userName) {
        Connection mysqlConnection = null;
        try {
            String connectionUrl = "jdbc:mysql://%1$s:3306/%2$s?useSSL=false"; //Google Cloud Database Public IP
            mysqlConnection = DriverManager.getConnection(String.format(connectionUrl, IP, DB), userName, "");
        } catch (Exception e) {
            e.printStackTrace();
        }
        return mysqlConnection;
    }
}
