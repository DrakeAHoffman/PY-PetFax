from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

pet_facts = {
    'Max': 'Max loves to play fetch!',
    'Kiko': 'Kiko enjoys long walks in the park.',
    'Thumper': 'Thumper is an expert at hopping around.'
}


@app.route('/pet/<pet_name>')
def show_pet(pet_name):
    if pet_name in pet_facts:
        fact = pet_facts[pet_name]
    else:
        fact = 'Sorry, information not available for this pet.'

    return render_template('pet_show.html', pet_name=pet_name, fact=fact)

@app.route('/facts', methods=['GET', 'POST'])
def facts():
    if request.method == 'POST':
        pet_name = request.form['pet_name']
        fun_fact = request.form['fun_fact']

       
        print(f"Submitted Fact: Pet Name - {pet_name}, Fun Fact - {fun_fact}")

      
        return redirect(url_for('facts'))

    return render_template('facts.html')

if __name__ == '__main__':
    app.run(debug=True)

