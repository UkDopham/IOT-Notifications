import { makeStyles } from '@material-ui/core/styles';
import { Theme } from '@material-ui/core';

export const useStyles = makeStyles<Theme>(theme =>
(
    {
        text: {
            margin: 5,
            padding: 5,
            fontWeight: "bold",
            fontSize: 35,
            color: "white"
        },
        buttonBig: {
            margin: 15,
            padding: 10,
            backgroundColor: "blue",
        },
        buttonSmall: {
            margin: 15,
            padding: 5,
            backgroundColor: "#477e5e",
            alignItems: "center",
            justifyContent: "center",
        },
        box: {
            textAlign: "center",
            margin: "10%",
            padding: "5%",
            backgroundColor: "#94ce98",
            borderRadius: 10,
            alignItems: "center",
            justifyContent: "center",
        },
        listItem: {
            alignItems: "center",
            justifyContent: "center",
        },
        avatar: {
            width: "20%",
            height: "20%"
        },
        title: {
            fontWeight: "bold",
            fontSize: 55,
            margin: 5,
        },
        subtitle: {
            margin: 5,
            fontSize: 35,
            color: "white"
        },
        input: {
            color: "white"
        }
    })
);