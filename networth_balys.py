import PySimpleGUI as sg


class Asset:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Investment(Asset):  # Inherit from Asset
    def __init__(self, name, price, roi):
        super().__init__(name, price)  # Call the constructor of the base class
        self.roi = roi
    
    def monthly_divident(self):
        yearly_roi = self.price * (self.roi/100)
        monthly_divident = yearly_roi / 12
        return monthly_divident

def create_layout():
    layout = [
        [sg.Column([
            [sg.Text('Asset list:', size=30)],
            [sg.Listbox(values=[], size=(30, 6), key='asset_list')],
            [sg.Text('Input new asset name and asset value')],
            [sg.InputText(key='new_asset', size=(20, 1)), sg.InputText(key='asset_price', size=(10, 1)), sg.Button('Add Asset')],
            [sg.Text('Input new investment name, investment value, and yearly return %')],
            [sg.InputText(key='new_investment', size=(20, 1)), sg.InputText(key='investment_price', size=(10, 1)),
             sg.InputText(key='investment_roi', size=(10, 1)), sg.Button('Add Investment')],
            [sg.Text('Enter new target'),sg.InputText(key='new_target', size=(20, 1))],
            [sg.Text('Total Net Worth: $', size=(15, 1)), sg.Text('', size=(15, 1), key='net_worth')],
            [sg.ProgressBar(max_value=100, orientation='horizontal', size=(40, 10), style='xpnative', key='progress_bar')],
            [sg.Text("Estimated Passive Income Next Month:"), sg.Text('$0', size=(20, 1), key='passive_income')],
            [sg.Text('Estimated months untill target:'), sg.Text('', size=(20, 1), key='months_until_target')],
            [sg.Button('Calculate progress'), sg.Button('Exit', button_color=('white', 'red'))]
        ], pad=(0, 0))]
    ]
    return layout

def update_net_worth(window, assets):
    net_worth = sum(asset.price for asset in assets)
    window['net_worth'].update(f'{net_worth:.2f}')

def update_net_worth_target(window, new_target: float):
    window['net_worth_target'].update(f'{new_target:.2f}')

def calculate_progress(window, assets, values):
    net_worth = sum(asset.price for asset in assets)
    new_target_input = values['new_target']
    try:
        net_worth_target = float(new_target_input)
        progress = (net_worth / net_worth_target) * 100
        return progress
    except ValueError:
        return None
    
def calculate_passive_income(window, assets):
    next_month_income = 0
    for asset in assets:
        if isinstance(asset, Investment):
            monthly_divident = asset.monthly_divident()
            next_month_income += monthly_divident
            passive_income_bar = window['passive_income']
            passive_income_bar.update(next_month_income)
    return next_month_income

def calculate_months_until_target(window, assets, values):
    months_until_target = 0
    target_input = values['new_target']
    current_net_worth = sum(asset.price for asset in assets)
    try:
        target_input = float(target_input)
    except ValueError:
        sg.popup_error('Please enter a valid target value FLOAT.')
        return None
    current_net_worth > target_input
    months_until_target = (target_input - current_net_worth) / calculate_passive_income(window, assets)
    months_until_target_bar = window['months_until_target']
    months_until_target_bar.update(round(months_until_target))
    return round(months_until_target)

            

def main():
    sg.theme('LightGrey1')
    assets = []  # Use a single list for both assets and investments

    layout = create_layout()
    window = sg.Window('Net Worth Tracker', layout, resizable=True)

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        if event == 'Add Asset':
            new_asset_name = values['new_asset']
            new_asset_price = values['asset_price']
            if new_asset_name and new_asset_price:
                try:
                    asset_price = float(new_asset_price)
                    assets.append(Asset(name=new_asset_name, price=asset_price))
                    window['asset_list'].update(values=[
                        f'{asset.name}: ${asset.price:.2f}, ROI: {asset.roi:.2f}%' if isinstance(asset, Investment)
                        else f'{asset.name}: ${asset.price:.2f}' for asset in assets
                    ])
                    window['new_asset'].update('')
                    window['asset_price'].update('')
                    update_net_worth(window, assets)
                except ValueError:
                    sg.popup_error('Please enter a valid asset price.')
            else:
                sg.popup_error('Please enter a valid asset name and price.')

        if event == 'Add Investment':
            new_investment_name = values['new_investment']
            new_investment_price = values['investment_price']
            new_investment_roi = values['investment_roi']
            if new_investment_name and new_investment_price and new_investment_roi:
                try:
                    investment_price = float(new_investment_price)
                    assets.append(Investment(name=new_investment_name, price=investment_price, roi=float(new_investment_roi)))
                    window['asset_list'].update(values=[
                        f'{asset.name}: ${asset.price:.2f}, ROI: {asset.roi:.2f}%' if isinstance(asset, Investment)
                        else f'{asset.name}: ${asset.price:.2f}' for asset in assets
                    ])
                    window['new_investment'].update('')
                    window['investment_price'].update('')
                    window['investment_roi'].update('')
                    update_net_worth(window, assets)
                except ValueError:
                    sg.popup_error('Please enter a valid Investment price.')
            else:
                sg.popup_error('Please enter a valid asset name and price and ROI.')

        if event == "Add Target":
            new_target_input = values['new_target']
            if new_target_input:
                try:
                    new_target_value = float(new_target_input)
                    update_net_worth_target(window, new_target_value)
                except ValueError:
                    sg.popup_error('Please enter a valid target value.')
            else:
                sg.popup_error('Please enter a target.')
        if event == 'Calculate progress':
            progress_bar = window['progress_bar']
            progress = calculate_progress(window, assets, values)
            if progress is not None:
                progress_bar.update(progress)
            else:
                sg.popup_error('Please enter a target.')

            calculate_passive_income(window, assets)
            calculate_months_until_target(window, assets, values)

    window.close()

if __name__ == '__main__':
    main()
