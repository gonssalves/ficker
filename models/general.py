from models.entities import Usuario, TransacaoEntrada, TransacaoSaida, Categoria
from flask import request, redirect, url_for, flash
from flask_login import current_user
from app import db
from sqlalchemy import exc
from datetime import datetime

def add_income():
    income_description = request.form.get('description')
    date = request.form.get('date')
    value = request.form.get('value')
    selected_option = request.form.get('selected_option')
    category_description = (request.form.get('new_category') if request.form.get('new_category') else 'Sem Categoria')
    
    date = datetime. strptime(date,  '%Y-%m-%d')

    user = Usuario.query.get(int(current_user.id))
   
    if selected_option == 'nova':

        query_category = Categoria.filter_by(dsc_categoria=category_description, usuario=user).first()

        if query_category:
            new_category = query_category    
        else:
            new_category = Categoria(dsc_categoria=category_description, usuario=user)
      
        new_income = TransacaoEntrada(dsc_entrada=income_description, dat_entrada=date, val_entrada=value, usuario=user, categoria=new_category)

        try:
            db.session.add_all([new_category, new_income])
            db.session.commit()
        except:
            flash('Não foi possível cadastrar sua entrada, por favor tente mais tarde')
            return redirect(url_for('main.incomes'))
    else:
        category = Categoria.query.filter_by(dsc_categoria=selected_option).first()
        new_income = TransacaoEntrada(dsc_entrada=income_description, dat_entrada=date, val_entrada=value, usuario=user, categoria=category)

        try:
            db.session.add(new_income)
            db.session.commit()
        except:
            flash('Não foi possível cadastrar sua entrada, por favor tente mais tarde')
            return redirect(url_for('main.incomes'))
        
    flash('Entrada cadastrada com sucesso')
    return redirect(url_for('main.incomes'))

def delete_income(old_income):
    try:
        db.session.delete(old_income)
        db.session.commit()
    except:
        flash('Não foi possível excluir a entrada, por favor tente mais tarde')
        return redirect(url_for('main.incomes'))
    
    flash('Entrada excluída')
    return redirect(url_for('main.incomes'))

def edit_income(old_income):
    return 'recurso não implementado ainda'

    income_description = request.form.get('description')
    date = request.form.get('date')
    value = request.form.get('value')
    selected_option = request.form.get('selected_option')
    category_description = (request.form.get('new_category') if request.form.get('new_category') else 'Sem Categoria')

    user = Usuario.query.get(int(current_user.id))

    category = Categoria.query.filter_by(dsc_categoria=selected_option).first()

    #edit_income = TransacaoEntrada.query.filter_by(dsc_entrada=income_description, dat_entrada=date, val_entrada=value, usuario=user, categoria=category).first()
    
    #return str(edit_income.id)
    
    old_income.dsc_entrada = income_description 
    old_income.dat_entrada = date 
    old_income.val_entrada = value 
    old_income.usuario = user 
    old_income.categoria = category

    try:
        db.session.add(old_income)
    except:
        flash('Não foi possível alterar a entrada, por favor tente mais tarde')
        return redirect(url_for('main.incomes'))
    
    db.session.commit()
    flash('Entrada alterada')
    return redirect(url_for('main.incomes'))


def add_expense():
    expense_description = request.form.get('description')
    date = request.form.get('date')
    value = request.form.get('value')
    
    date = datetime. strptime(date,  '%Y-%m-%d')

    user = Usuario.query.get(int(current_user.id))

    new_expense = TransacaoSaida(dsc_saida=expense_description, dat_saida=date, val_saida=value, usuario=user)

    try:
        db.session.add(new_expense)
        db.session.commit()
    except:
        flash('Não foi possível cadastrar sua saída, por favor tente mais tarde')
        return redirect(url_for('main.incomes'))
        
    flash('Saída cadastrada com sucesso')
    return redirect(url_for('main.expenses'))

def delete_expense(old_expense):
    try:
        db.session.delete(old_expense)
        db.session.commit()
    except:
        flash('Não foi possível excluir a saída, por favor tente mais tarde')
        return redirect(url_for('main.expenses'))
    
    flash('Saída excluída')
    return redirect(url_for('main.expenses'))

def edit_expense(old_expense):
    return 'recurso não implementado ainda'

    income_description = request.form.get('description')
    date = request.form.get('date')
    value = request.form.get('value')
    selected_option = request.form.get('selected_option')
    category_description = (request.form.get('new_category') if request.form.get('new_category') else 'Sem Categoria')

    user = Usuario.query.get(int(current_user.id))

    category = Categoria.query.filter_by(dsc_categoria=selected_option).first()

    #edit_income = TransacaoEntrada.query.filter_by(dsc_entrada=income_description, dat_entrada=date, val_entrada=value, usuario=user, categoria=category).first()
    
    #return str(edit_income.id)
    
    old_income.dsc_entrada = income_description 
    old_income.dat_entrada = date 
    old_income.val_entrada = value 
    old_income.usuario = user 
    old_income.categoria = category

    try:
        db.session.add(old_income)
    except:
        flash('Não foi possível alterar a entrada, por favor tente mais tarde')
        return redirect(url_for('main.incomes'))
    
    db.session.commit()
    flash('Entrada alterada')
    return redirect(url_for('main.incomes'))
    