import React from "react";
import "./index.css";



export default function Formulario(){

    return(
        <form className="form-card" method="post">
          <input type="hidden" value="postar" name="post" />
          <input
            className="form-card-title"
            type="text"
            name="titulo"
            placeholder="Título"
          />
          <textarea
            className="autoresize"
            name="detalhes"
            placeholder="Digite o conteúdo..."
          ></textarea>
          <textarea
            className="autoresize_zero"
            name="tag"
            id="tag"
            placeholder="Tag da nota"
          ></textarea>
          <button className="btn" type="submit">Criar</button>
        </form>
    )

}