import React, { Component } from "react"

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      viewCompleted: false,
      projects: []
      };
  }

    async componentDidMount() {
      try {
        const res = await fetch('http://127.0.0.1:8000/portfolio/api/project-api/');
        const projects = await res.json();
        this.setState({
          projects
        });
      } catch (e) {
        console.log(e);
    }
    }
    renderItems = () => {
      return newItems.map(item => (
        <div class="bgrid folio-item" id="projects">
        <div class="item-wrap" id="modal_1" >
           <img id="image_project" src="" alt="Liberty">
           <a data-id="" href="#modal-01" class="overlay" id="get">	                  	           
            <div class="folio-item-table">
              <div class="folio-item-cell">
                  <h3 class="folio-title" id="title_project"></h3>	     					    
                   <span class="folio-types">
                     Web Developer
                  </span>
                </div>	                      	
             </div>                    
          </a>
        </div>	         
    </div>
      ));
    };

    render() {
      return (
        <main className="content">
        <div className="row">
          <div className="col-md-6 col-sm-10 mx-auto p-0">
            <div className="card p-3">
              <ul className="list-group list-group-flush">
                {this.renderItems()}
              </ul>
            </div>
          </div>
        </div>
      </main>
      )
    }
  }
  
export default App;