from flask import Flask, url_for

app = Flask(__name__)


@app.route('/carousel')
def carousel():
    return f'''<!doctype html>
                    <html lang="en">
                        <head>
                          <meta charset="utf-8">
                          <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                          <link rel="stylesheet"
                          href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                          integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                          crossorigin="anonymous">
                          <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                          <title>Пример формы</title>
                        </head>
                        <body>
                          <h1 align="center">Пейзажи Марса<h1>
                          <section class="carousel" aria-label="Gallery">
                            <ol class="carousel__viewport">
                                  <li id="carousel__slide1"
                                      tabindex="0"
                                      class="carousel__slide">
                                    <div class="carousel__snapper">
                                      <a href="#carousel__slide4"
                                         class="carousel__prev">Go to last slide</a>
                                         <img src="/static/img/mar.jpg" width=570 height=405>
                                      <a href="#carousel__slide2"
                                         class="carousel__next">Go to next slide</a>
                                    </div>
                                  </li>
                                  <li id="carousel__slide2"
                                      tabindex="0"
                                      class="carousel__slide">
                                    <div class="carousel__snapper"></div>
                                    <a href="#carousel__slide1"
                                       class="carousel__prev">Go to previous slide</a>
                                       <img src="/static/img/mar1.png" width=570 height=405>
                                    <a href="#carousel__slide3"
                                       class="carousel__next">Go to next slide</a>
                                  </li>
                                  <li id="carousel__slide3"
                                      tabindex="0"
                                      class="carousel__slide">
                                    <div class="carousel__snapper"></div>
                                    <a href="#carousel__slide2"
                                       class="carousel__prev">Go to previous slide</a>
                                       <img src="/static/img/mar2.jpg" width=570 height=405>
                                    <a href="#carousel__slide4"
                                       class="carousel__next">Go to next slide</a>
                                  </li>
                                  <li id="carousel__slide4"
                                      tabindex="0"
                                      class="carousel__slide">
                                    <div class="carousel__snapper"></div>
                                    <a href="#carousel__slide3"
                                       class="carousel__prev">Go to previous slide</a>
                                       <img src="/static/img/mar3.jpg" width=570 height=405>
                                    <a href="#carousel__slide1"
                                       class="carousel__next">Go to first slide</a>
                                  </li>
                            </ol>
                                <aside class="carousel__navigation">
                                  <ol class="carousel__navigation-list">
                                    <li class="carousel__navigation-item">
                                      <a href="#carousel__slide1"
                                         class="carousel__navigation-button">Go to slide 1</a>
                                    </li>
                                    <li class="carousel__navigation-item">
                                      <a href="#carousel__slide2"
                                         class="carousel__navigation-button">Go to slide 2</a>
                                    </li>
                                    <li class="carousel__navigation-item">
                                      <a href="#carousel__slide3"
                                         class="carousel__navigation-button">Go to slide 3</a>
                                    </li>
                                    <li class="carousel__navigation-item">
                                      <a href="#carousel__slide4"
                                         class="carousel__navigation-button">Go to slide 4</a>
                                    </li>
                                  </ol>
                                </aside>
                          </section>
                        </body>
                    </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
