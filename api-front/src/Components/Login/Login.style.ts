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
        },
        buttonBig: {
            margin: 15,
            padding: 10,
            backgroundColor: "blue",
        },
        buttonSmall: {
            margin: 15,
            padding: 5,
            backgroundColor: "green",
            alignItems: "center",
            justifyContent: "center",
        },
        box: {
            textAlign: "center",
            margin: "20%",
            padding: "10%",
            backgroundColor: "yellow",
            borderRadius: 10,
            alignItems: "center",
            justifyContent: "center",
        },
        listItem : {
            alignItems: "center",
            justifyContent: "center",
        }
    })
);