import { CommonModule } from '@angular/common';
import { Component, Input, OnInit } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { Servicios } from '../../../../interfaces/planes/servicios.interface';
import { Ciudades } from '../../../../interfaces/places/ciudad.interface';
import { TariffPlanes, TariffPlanesVariant } from '../../../../interfaces/planes/tariffplanes.interface';
import { CommunicationDataService } from '../../../../services/communication/communicationData.service';
import { Buro } from '../../../../interfaces/financial/buro.interface';
import { ModosPago } from '../../../../interfaces/financial/modos-pago.interface';
import { Sectores } from '../../../../interfaces/places/sector.interface';
import { FdCombosService } from '../../../../services/fetchData/fd-combos.service';
import { FdPlacesService } from '../../../../services/fetchData/fd-places.service';
import { FdModospagosService } from '../../../../services/fetchData/FinancialInfo/fd-modospagos.service';
import { FdBuroService } from '../../../../services/fetchData/FinancialInfo/fd-buro.service';
import { Productos } from '../../../../interfaces/planes/productos.interface';
import { DiasGozados } from '../../../../interfaces/DataPromocional/dias-gozados.interface';
import { FdDiasGozadosService } from '../../../../services/fetchData/DataPromocional/fd-dias_gozados.service';
import { FdPrecioRegularService } from '../../../../services/fetchData/DataPromocional/fd-precio_regular.service';
import { PrecioRegular } from '../../../../interfaces/DataPromocional/precio-regular.interface';
import { FdUpgradeService } from '../../../../services/fetchData/DataPromocional/fd-upgrade.service';
import { Upgrade } from '../../../../interfaces/DataPromocional/upgrade.interface';
import { Options_PA } from '../../../../interfaces/Interfaces-View/Options_PA.interface';

@Component({
  selector: 'app-table-insert',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './table-insert.component.html',
  styleUrl: './table-insert.component.scss'
})
export class TableInsertComponent implements OnInit {  
  @Input() rows: any[] = [];
  _V1: string = ''; _V2: string = ''; _V3: string = ''; 
  _V4: string = ''; _V9: string = ''; _V11: string = '';

  //v. Estructura de datos
  serviciosData: Servicios[] = [];
  productosData: Productos[][] = [];
  planData: TariffPlanes[][] = [];
  planVData: TariffPlanesVariant[][] = [];
  ciudadData: Ciudades[][] = [];
  sectoresData: Sectores[][] = [];
  buroData: Buro[][] = [];
  modoPagosData: ModosPago[][] = [];
  diasGozadosData: DiasGozados[][] = [];
  precioRegularData: PrecioRegular[][] = [];
  upgradeData: Upgrade [][] = [];
  optionsData: Options_PA[][] = [];

  showMDPDD: boolean[] = []; 
  showBDD: boolean[] = [];
  showPROAD: boolean[] = [];
  visibleBtnPromocionAdicional: boolean[] = [];
  closing: boolean = false;

  modal_cs: boolean = false;
  modal_dp: boolean = false;
  rowId: number = 0;
 
  constructor(
    private comData: CommunicationDataService,
    private fdpl: FdPlacesService,
    private fdcb: FdCombosService,
    private fdmp: FdModospagosService,
    private fdb: FdBuroService,
    private fddg: FdDiasGozadosService,
    private fdpr: FdPrecioRegularService,
    private fdup: FdUpgradeService
  ){}

  ngOnInit(): void {
    this.addRow(); // Añade la primera fila automáticamente al cargar
    this.comData.dServicios$.subscribe(data => {this.serviciosData = data;});
  }

  addRow(): void {
    const newRow = {
      id: this.rows.length,
      _V1: '', _V2: '', _V3: '', _V4: '', _V9: '', _V11: '',
      planData: [], planVData: [], productosData: [], ciudadData: [], sectoresData: [],
      diasGozadosData: [], upgradeData: []
    };
    this.rows.push(newRow); // Añade el nuevo objeto al array de filas
    this.planData.push([]);
    this.planVData.push([]);
    this.productosData.push([]); 
    this.upgradeData.push([]);
    this.getModoPagosData(this.rows.length - 1);
    this.getBuroData(this.rows.length - 1)
    this.ciudadData.push([]);
    this.sectoresData.push([]);
    this.upgradeData.push([]);
    this.showMDPDD.push(false);
    this.showBDD.push(false);
    this.showPROAD.push(false);
    this.optionsData.push([
      {name: 'NO APLICAR', selected: false},
      {name: 'STREAMING', selected: false},
      {name: 'TELEFONIA', selected: false},
      {name: 'TELEVISION', selected: false},
      {name: 'ROUTER', selected: false}

    ]);
  }

  getDataPLAN(servicio: string, index: number): void {
    try {
      if(servicio){
        this.fdcb.getComboPLAN_RETURN(servicio).subscribe((plan: TariffPlanes[]) => {
          this.planData[index] = plan;
        })
      }
    } catch (error) {
      console.log("Error detectado: ",error)
    }
  }

  getDataPLANVARIANT(id_Plan: number, index: number): void {
    try {
      if(id_Plan){
        this.fdcb.getComboPLANVARIANT_RETURN(id_Plan).subscribe((planv: TariffPlanesVariant[]) => {
          this.planVData[index] = planv;
        });
      }
    } catch (error) {
      console.log("Error Detectado: ",error)
    }
  }

  getDataPROD(TPV: number, index: number): void {
    try {
      if(TPV){
        this.fdcb.getComboPROD_RETURN(TPV).subscribe((prod: Productos[]) => {
          this.productosData[index] = prod;
        });
      }
    } catch(error){
      console.log("Error Detectado: ",error)
    }
  }

  getCiudadesTariffplanVariant(TPV: number, index: number): void {
    try {
      this.fdpl.fetchDataCiudadesALLXTariffplanVariant_RETURN(TPV).subscribe((city: Ciudades[]) => {
        this.ciudadData[index] = city;
      });
    } catch(error){
      console.log("Error Detectado: ",error)
    }
  }

  getModoPagosData(index: number): void {
    try {
      this.fdmp.fetchDataModosPago_RETURN().subscribe((modosPago) => {
        this.modoPagosData[index] = modosPago;
      });
    } catch (error) {
      console.log("Error detectado: ",error)
    }
  }
  
  getBuroData(index: number): void{
    try {
      this.fdb.fetchDataBuro_RETURN().subscribe((buro) => {
        this.buroData[index] = buro;
      });
    } catch (error) {
      console.log("Error detectado: ",error)
    }
  }

  getDiasGozados(index: number): void {
    try {
      this.fddg.getDiasGozados_RETURN().subscribe((digd) => {
        this.diasGozadosData[index] = digd;
      })
    } catch (error) {
      console.log("Error detectado: ",error)
    }
  }

  getPrecioRegular(id_Producto: number, TPV: number, index: number): void {
    try{
      if (id_Producto && TPV){
        this.fdpr.getPrecioRegular_RETURN(id_Producto, TPV).subscribe((prec) => {
          this.precioRegularData[index] = prec;
        })
      }
    } catch (error) {
      console.log("Error detectado: ",error)
    }
  }

  getDataUpgrade(tariffplanes: number, TFPV: number, index: number): void {
    try{
      if (tariffplanes && TFPV){
        this.fdup.getUpgrade_RETURN(tariffplanes, TFPV).subscribe((upgr) => {
          this.upgradeData[index] = upgr
        })
      }
    } catch (error) {
      console.log("Error detectado: ",error)
    }
  }

  buscarSectores() {
    const index = this.rowId;
    const indexRow = this.rows[index];
    const _V3 = indexRow._V3;
    const ciudades = this.ciudadData[index].filter(city => city.selected).map(city => city.CIUDAD_ID);
    this.fdpl.fetchDataSectoresMasivosXTariffplanVariant_RETURN(ciudades, _V3)
    .subscribe((sectores) => {
      this.sectoresData[index] = sectores;
    });
  }

  button_V1_V6(row: any, index: number): boolean {
    const trueSelect = row._V1 && row._V2 && row._V3 && row._V4;
    const trueMP = this.modoPagosData[index] && this.modoPagosData[index].some(mdpg => mdpg.selected);
    const trueB = this.buroData[index] && this.buroData[index].some(buro => buro.selected);
    return trueSelect && trueMP && trueB;
  }

  getDataPAPrecioRegularTTR(type: string, TFPV: number, index: number): void {
    if(TFPV){
      switch(type){
        case 'STREAMING':
        break;
        case 'TELEFONIA':
        break;
        case 'TELEVISION':
        break;
        case 'ROUTER':
        break;
      }
    }
  }

  visibleBotonPromocionAdicional(servicio: string, index: number): void {
    if (servicio && servicio == 'STREAMING') {
      this.visibleBtnPromocionAdicional[index] = true;
    } else {
      this.visibleBtnPromocionAdicional[index] = false;
    }
  }

  button_search_sect(index: number): boolean {
    const trueCiudadList = this.ciudadData[index].some(ciudad => ciudad.selected);
    return trueCiudadList;
  }

  button_V1_V8(row: any, index: number): boolean {
    const trueSelect = row._V1 && row._V2 && row._V3 && row._V4;
    const trueMP = this.modoPagosData[index] && this.modoPagosData[index].some(mdpg => mdpg.selected);
    const trueB = this.buroData[index] && this.buroData[index].some(buro => buro.selected);
    const trueC = this.ciudadData[index] && this.ciudadData[index].some(ciudad => ciudad.selected);
    const trueS = this.sectoresData[index] && this.sectoresData[index].some(sectores => sectores.selected);
    return trueSelect && trueMP && trueB && trueC && trueS;
  }

  toggDD(index: number, type: string) {
    switch(type){
      case 'MP':
        if (this.showMDPDD) {
          this.closing = true;// Si está abierto y se va a cerrar, activa la transición rápida
          setTimeout(() => {
            this.showMDPDD[index] = !this.showMDPDD[index];
            this.closing = false;
          }, 30); // Espera el tiempo de la transición de cierre
        }
      break;
      case 'B':
        if (this.showBDD) {
          this.closing = true;// Si está abierto y se va a cerrar, activa la transición rápida
          setTimeout(() => {
            this.showBDD[index] = !this.showBDD[index];
            this.closing = false;
          }, 30); // Espera el tiempo de la transición de cierre
        }
      break;
      case 'PA':
        if (this.showPROAD) {
          this.closing = true;
          setTimeout(() => {
            this.showPROAD[index] = !this.showPROAD[index];
            this.closing = false;
          }, 30); // Espera el tiempo de la transición de cierre
        }
      break;
    }
  }

  checkSDLoading() {
    return this.serviciosData.length === 0;
  }

  openModal(row: number, type: string): void {
    this.rowId = row;
    switch(type){
      case 'CS':
        this.modal_cs = true;
      break;
      case 'DP':
        this.modal_dp = true;
      break;
    }
  }

  closeModal(type: string): void {
    switch(type){
      case 'CS':
        this.modal_cs = false;
      break;
      case 'DP':
        this.modal_dp = false;
      break;
    }
  }

  updateSelection(rowId: number, index: number): void {
    const options = this.optionsData[rowId];
  
    if (index === 0 && options[0].selected) {
      // "NO APLICAR" ha sido seleccionado
      options.forEach((option, idx) => {
        if (idx !== 0) option.selected = false;
      });
    } else if (index !== 0 && options[index].selected) {
      // Otra opción que no es "NO APLICAR" ha sido seleccionada
      options[0].selected = false;
    }
  }
}